"""The Option C split must be lossless, checked against the real tree rather than a fixture.

The oracle is `decompose(compose(content))`, not `content/` itself, because the committed
tree is not a fixed point of its own round-trip: 274 of 15,192 files differ after
`decompose(compose(content))` — 268 `_index.md` files whose committed copies end with a
newline the generator does not emit, 2 `document.md` files where an apostrophe in the name
makes the YAML emitter quote it (`name: Stablewatch's …` vs `name: "Stablewatch's …"`,
parsing identically either way), and 3 directories (`A/1/10/1/5`, `A/1/13/1/5`, `A/1/9/4`)
holding only an `_index.md` or an empty subdirectory that the generator would never
produce. Document count reconciles exactly, so nothing is lost; this is drift between the
committed tree and the tooling.

Asserting a byte-exact round-trip against `content/` would therefore fail regardless of
the split. Comparing the split path against the monolith path isolates the behaviour under
test and is unaffected by that drift.

The invariants, strongest first:
  1. reassemble(split(x)) == compose(x)          — byte-identical markdown
  2. decompose_multi(split(x)) == decompose(compose(x))  — byte-identical tree
Invariant 2 follows from 1, and is asserted anyway because it is the property consumers
depend on and a refactor could break the chain between them without breaking 1.
"""
from __future__ import annotations

import filecmp
import inspect
import os
import subprocess
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from collections import Counter                        # noqa: E402

from compose import compose, compose_segments          # noqa: E402
from decompose import HEADING_RE, Document, decompose  # noqa: E402
from decompose_multi import reassemble                 # noqa: E402
from partition import (MAX_HEADING_LEVEL, bucket_for,  # noqa: E402
                       canonical_sort_key, order_documents, order_key,
                       restore_absolute_levels, set_heading_level,
                       structural_depth, split, write_split)

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONTENT = os.path.join(_REPO, "content")


def _atomized_tree() -> str | None:
    """An atomized tree to test against, whichever layout the repo is actually in.

    `split()` consumes an atomized tree, so once `content/` holds the consolidated files
    there is nothing left to split and every invariant here would start skipping silently.

    Post-cutover the atomized form is one round-trip away: compose the consolidated files
    and decompose the result. Deriving the fixture that way keeps the invariants running
    in either layout.
    """
    if not os.path.isdir(_CONTENT):
        return None
    from atlas_source import ATOMIZED, detect_layout, load_composed
    if detect_layout(_CONTENT) == ATOMIZED:
        return _CONTENT
    tmp = tempfile.mkdtemp(prefix="atlas-atomized-fixture-")
    md = os.path.join(tmp, "composed.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write(load_composed(_CONTENT))
    out = os.path.join(tmp, "content")
    decompose(md, out)
    return out


CONTENT = _atomized_tree()

pytestmark = pytest.mark.skipif(
    CONTENT is None, reason="no content/ in either layout")


# ---------------------------------------------------------------------------
# Bucketing rule
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("doc_no,expected", [
    ("A.0", "A.0"),
    ("A.1", "A.1"),
    ("A.1.10.2.3", "A.1"),
    ("A.5.1", "A.5"),
    # The Agent Scope spine — containers that belong to NO agent. Every
    # `List Of … Agent Artifacts` Section is spine, including A.6.1.2.
    ("A.6", "A.6"),
    ("A.6.1", "A.6"),
    ("A.6.1.1", "A.6"),
    ("A.6.1.2", "A.6"),
    # Agents are individually filed, whatever their type, and carry their subtree.
    ("A.6.1.1.1", "A.6.1.1.1"),
    ("A.6.1.1.1.2.6.3", "A.6.1.1.1"),
    ("A.6.1.1.8", "A.6.1.1.8"),
    ("A.6.1.2.1", "A.6.1.2.1"),
    ("A.6.1.2.3", "A.6.1.2.3"),
    ("A.6.1.2.3.1", "A.6.1.2.3"),
    # Growth of all three kinds, with no code change: a ninth Prime, a fourth Executor,
    # and an entirely new agent type whose Section stays in A.6 while its children each
    # get a file.
    ("A.6.1.1.9", "A.6.1.1.9"),
    ("A.6.1.1.10", "A.6.1.1.10"),
    ("A.6.1.1.10.4.2", "A.6.1.1.10"),
    ("A.6.1.2.4", "A.6.1.2.4"),
    ("A.6.1.3", "A.6"),
    ("A.6.1.3.1", "A.6.1.3.1"),
    ("A.6.1.3.1.2.2", "A.6.1.3.1"),
])
def test_bucket_for(doc_no, expected):
    assert bucket_for(doc_no) == expected


def test_no_agent_or_agent_type_is_named_in_the_partition_rule():
    """The partition rule must stay structural, so that onboarding an agent needs no edit
    here. Agents are identified by position (`A.6.1.<type>.<agent>`), never by identity,
    and this fails if a `PRIME_ARTIFACT_PARENT` / `EXECUTOR_BUCKET` pair or a list of Star
    names is reintroduced.
    """
    import partition
    # Only the executable body — the docstring cites doc numbers as illustration.
    src = inspect.getsource(partition.bucket_for)
    head, _, rest = src.partition('"""')
    code = head + rest.partition('"""')[2]
    for name in ("Spark", "Grove", "Keel", "Skybase", "Obex", "Pattern", "Osero",
                 "Amatsu", "Ozone", "A.6.1.1", "A.6.1.2"):
        assert name not in code, (
            f"bucket_for's code mentions {name!r} — the partition rule must be derived "
            "from document position, not from an enumeration of agents or agent types."
        )


def test_nr_inherits_previous_bucket():
    """NRs are emitted inline under their placement target and have no position of
    their own, so they must not claim a bucket."""
    assert bucket_for("NR-42") is None


# ---------------------------------------------------------------------------
# The spine guard
# ---------------------------------------------------------------------------

def test_agent_scope_spine_is_its_own_bucket_and_is_not_empty():
    """`A.6`, `A.6.1` and `A.6.1.1` sit in the Agent Scope above every artifact. Fanning
    them into an artifact, or dropping them, still leaves every other document with a
    home, so the total document count reconciles and no count-based check detects the
    loss.
    """
    _lines, runs, _names = split(CONTENT)
    spine_docs = sum(r["docs"] for r in runs if r["bucket"] == "A.6")
    assert spine_docs == 4, (
        f"the A.6 Agent Scope bucket holds {spine_docs} documents, expected the 4 spine "
        "containers (A.6, A.6.1, A.6.1.1, A.6.1.2). If the Atlas genuinely gained a "
        "container here — a new agent type adds one — update this number deliberately. "
        "Do not delete the assertion."
    )


def test_the_executor_list_lives_in_the_agent_scope_file():
    """`A.6.1.1` and `A.6.1.2` are both Sections and structurally identical siblings, so
    `A.6.1.2 - List Of Executor Agent Artifacts` belongs in the Agent Scope file rather
    than in a file of its own. Grouping it there interrupts the `A.6` bucket with the
    Prime Agent files, which document-level ordering allows.
    """
    lines_by_bucket, _runs, _names = split(CONTENT)
    assert "A.6.1.2" not in lines_by_bucket, (
        "A.6.1.2 has its own bucket again — it is a List document, not an Agent, and "
        "belongs in the A.6 file exactly as A.6.1.1 does."
    )
    agent_scope = "\n".join(lines_by_bucket["A.6"])
    assert "A.6.1.2 - List Of Executor Agent Artifacts" in agent_scope
    # ...and each Executor Agent beneath it is filed on its own, like a Prime Agent.
    for agent in ("A.6.1.2.1", "A.6.1.2.2", "A.6.1.2.3"):
        assert agent in lines_by_bucket, f"{agent} is an Agent and needs its own file"


def test_a_bucket_may_be_non_contiguous_and_a_6_actually_is():
    """A bucket need not occupy one unbroken run of the composed stream, and `A.6` does
    not: emit order is `A.6, A.6.1, A.6.1.1, [8 Primes], A.6.1.2, [3 Executors]`, so the
    spine is two runs with every Prime Agent file in between.

    The fragmentation grows with the Atlas. Each new agent type adds another `List Of …`
    Section emitted after the previous type's agents, adding one further run per type.
    """
    _lines, runs, _names = split(CONTENT)
    a6_runs = [r for r in runs if r["bucket"] == "A.6"]
    assert len(a6_runs) == 2, (
        f"expected the A.6 spine to be split into 2 runs by the Prime Agent files, got "
        f"{len(a6_runs)}. If this changed, the Agent Scope structure changed."
    )
    assert len(runs) > len({r["bucket"] for r in runs}), (
        "no bucket is non-contiguous — this test is meant to exercise the case that the "
        "old bucket-order reassembly could not express."
    )


def test_order_survives_a_tenth_agent():
    """Filename sorting breaks once a tenth agent exists: lexicographic order puts
    `A.6.1.1.10` between `.1` and `.2`. The integer-tuple key does not."""
    agents = [f"A.6.1.1.{i}" for i in (1, 2, 9, 10, 11)]
    assert sorted(agents, key=order_key) == agents
    assert sorted(agents) != agents, "filename sort is expected to be wrong here"


# ---------------------------------------------------------------------------
# Document ordering
# ---------------------------------------------------------------------------

def test_canonical_key_reproduces_composes_emit_order_exactly():
    """Reassembly derives each document's position from its doc number alone. A
    derivation disagreeing with compose anywhere would reorder documents silently, so it
    is checked over every numbered document in the tree.
    """
    segments = compose_segments(CONTENT)
    emitted = [d.doc_no for d, _ in segments if not d.doc_no.startswith("NR-")]
    real = set(emitted)
    assert sorted(emitted, key=lambda dn: canonical_sort_key(dn, real)) == emitted


def test_naive_doc_number_sorting_is_wrong_and_stays_rejected():
    """Compose emits a parent's real children before any subtree rooted at a phantom
    extension folder (the `0/` dirs that carry no document.md and exist only to give
    Action Tenets and Annotations the right heading depth), so `A.1.1.1` legitimately
    precedes `A.1.1.0.3.1`.

    Ascending doc-number order gets that backwards in hundreds of places. Reducing
    `canonical_sort_key` to a plain integer-tuple sort therefore fails here rather than
    reordering the Atlas silently.
    """
    segments = compose_segments(CONTENT)
    emitted = [d.doc_no for d, _ in segments if not d.doc_no.startswith("NR-")]

    def naive(dn):
        return tuple(int(s) if s.isdigit() else -1 for s in dn.split(".")[1:])

    divergences = sum(1 for a, b in zip(sorted(emitted, key=naive), emitted) if a != b)
    assert divergences > 100, (
        f"naive doc-number sorting diverged from compose in only {divergences} places. "
        "It diverges in 410 places on the current Atlas; if that collapsed to zero the "
        "phantom extension folders are gone and canonical_sort_key can be revisited."
    )


def test_needed_research_stays_attached_to_its_placement_target():
    """An NR has no position of its own: its number comes from a flat `NR-<n>` namespace,
    and post-consolidation its target is defined by its position (`decompose` derives
    `targets[0]` as the most recently seen numbered document). Sorting NRs as documents
    would scatter them and retarget every one.

    NRs are therefore never sorted: `partition.Block` carries each one inside its target's
    block. This asserts the resulting adjacency survives a full split/reassemble round
    trip.
    """
    def nr_targets(text):
        out, last = {}, None
        for line in text.split("\n"):
            m = HEADING_RE.match(line)
            if not m:
                continue
            doc_no = m.group(2)
            if doc_no.startswith("NR-"):
                out[doc_no] = last
            else:
                last = doc_no
        return out

    expected = nr_targets(compose(CONTENT))
    assert expected, "no NR documents found — this test would be vacuous"
    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        assert nr_targets(reassemble(d)) == expected


def test_reassembly_ignores_the_order_files_are_given_in():
    """Reassembly must depend on the documents, not on directory listing order, filename
    sorting, or bucket order. Shuffling the input mapping must change nothing."""
    lines_by_bucket, _runs, _names = split(CONTENT)
    forward = order_documents(lines_by_bucket)
    reversed_in = dict(reversed(list(lines_by_bucket.items())))
    assert order_documents(reversed_in) == forward


def test_a_document_in_two_files_is_rejected():
    """Duplication would make ordering ambiguous and silently emit a document twice."""
    lines_by_bucket, _runs, _names = split(CONTENT)
    poisoned = dict(lines_by_bucket)
    poisoned["A.6-copy"] = list(lines_by_bucket["A.6"])
    with pytest.raises(ValueError, match="appears in both"):
        order_documents(poisoned)


def test_every_document_lands_in_exactly_one_bucket():
    segments = compose_segments(CONTENT)
    _lines, runs, _names = split(CONTENT)
    assert sum(r["docs"] for r in runs) == len(segments)


# ---------------------------------------------------------------------------
# Heading levels
# ---------------------------------------------------------------------------

def _headings(text: str) -> list[tuple[int, str]]:
    """Every Atlas heading in a stream, as (level, doc number)."""
    out = []
    for line in text.split("\n"):
        m = HEADING_RE.match(line)
        if m:
            out.append((len(m.group(1)), m.group(2)))
    return out


def _split_headings() -> dict[str, list[tuple[int, str]]]:
    """Headings per bucket file, with the levels the files are written with."""
    lines_by_bucket, _runs, _names = split(CONTENT)
    return {b: _headings("\n".join(lines)) for b, lines in lines_by_bucket.items()}


def test_structural_depth_reproduces_composes_level_for_every_document():
    """Reassembly re-derives each heading's absolute level from doc numbers, the way it
    derives order. A derivation disagreeing with compose anywhere would change the composed
    Atlas, so it is checked over every numbered document in the tree.
    """
    segments = compose_segments(CONTENT)
    real = {d.doc_no for d, _ in segments if not d.doc_no.startswith("NR-")}
    for d, lines in segments:
        if d.doc_no.startswith("NR-"):
            continue
        expected = len(lines[0].split(" ", 1)[0])
        assert min(structural_depth(d.doc_no, real) + 1, MAX_HEADING_LEVEL) == expected, (
            f"{d.doc_no} derives level "
            f"{min(structural_depth(d.doc_no, real) + 1, MAX_HEADING_LEVEL)} "
            f"but compose emits {expected}"
        )


def test_counting_doc_number_segments_is_wrong_and_stays_rejected():
    """Depth is the number of ancestors that exist, not the number of doc number segments.
    A segment can be a phantom extension folder holding no document, and the leading `A` is
    phantom too, so segment counting runs deep.

    It is wrong in over a thousand places, including every Scope. Reducing
    `structural_depth` to a segment count therefore fails here rather than silently
    deepening the Atlas.
    """
    segments = compose_segments(CONTENT)
    divergences = 0
    for d, lines in segments:
        if d.doc_no.startswith("NR-"):
            continue
        by_segments = Document(doc_no=d.doc_no, name=d.name, doc_type=d.doc_type,
                               uuid=d.uuid, heading_level=0).output_heading_level
        if by_segments != len(lines[0].split(" ", 1)[0]):
            divergences += 1
    assert divergences > 1000, (
        f"segment counting diverged from compose in only {divergences} places. It diverges "
        "in 1,132 places on the current Atlas; if that collapsed to zero the phantom "
        "extension folders are gone and structural_depth can be revisited."
    )


def test_every_file_starts_at_heading_level_one():
    """The point of file-relative levels: a file opens at the top of the heading range
    rather than at the depth its subtree happens to sit at in the whole Atlas.
    """
    for bucket, heads in _split_headings().items():
        level, doc_no = heads[0]
        assert level == 1, f"{bucket} opens at level {level} with {doc_no}"


def test_levels_inside_a_file_step_down_one_per_ancestor():
    """Within a file each document sits one level below its nearest ancestor also in that
    file, and the file's root sits at 1. Levels stop deepening at 6, the deepest level
    markdown has.
    """
    for bucket, heads in _split_headings().items():
        level_of: dict[str, int] = {}
        for level, doc_no in heads:
            if doc_no.startswith("NR-"):
                continue
            parts = doc_no.split(".")
            parent = None
            for i in range(len(parts) - 1, 0, -1):
                candidate = ".".join(parts[:i])
                if candidate in level_of:
                    parent = candidate
                    break
            expected = (1 if parent is None
                        else min(level_of[parent] + 1, MAX_HEADING_LEVEL))
            assert level == expected, (
                f"{doc_no} is at level {level} in {bucket}, expected {expected}"
                + (f" one below {parent}" if parent else " as the file's root")
            )
            level_of[doc_no] = level


def test_capped_documents_are_recapped_rather_than_shifted():
    """Nine documents in ten are already at the six-hash cap, so the cap — not the arithmetic
    — decides their level. Shifting a file's headings up frees some of them from the cap;
    restoring absolute levels must put every one of them back at 6 rather than at whatever
    a stored hash count plus an offset would give.
    """
    absolute = dict((dn, lv) for lv, dn in _headings(compose(CONTENT)))
    capped = {dn for dn, lv in absolute.items() if lv == MAX_HEADING_LEVEL}
    assert len(capped) > 10_000, "the cap is expected to dominate this Atlas"

    in_files = {dn: lv for heads in _split_headings().values() for lv, dn in heads}
    freed = [dn for dn in capped if in_files[dn] < MAX_HEADING_LEVEL]
    assert len(freed) > 500, (
        f"only {len(freed)} capped documents came out from under the cap in their own "
        "file; the re-capping this test guards is then untested"
    )

    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        restored = _headings(reassemble(d))

    assert all(lv == MAX_HEADING_LEVEL for lv, dn in restored if dn in capped)
    assert Counter(lv for lv, _dn in restored) == Counter(absolute.values()), (
        "the restored level histogram differs from compose's. An off-by-one in the "
        "re-derivation moves thousands of documents on or off the cap while leaving the "
        "shallow documents right."
    )


def test_absolute_levels_are_re_derived_not_read_from_the_files():
    """Levels come from doc numbers, never from the hashes in the file being read. Flatten
    every heading in every file to a single `#` and the composed Atlas must still come back
    unchanged, hash for hash.

    Reading the hashes cannot work even without this test: at the cap they no longer say
    how deep their document is.
    """
    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        for fname in os.listdir(d):
            path = os.path.join(d, fname)
            with open(path, encoding="utf-8") as f:
                lines = f.read().split("\n")
            flattened = [set_heading_level(ln, 1) if HEADING_RE.match(ln) else ln
                         for ln in lines]
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(flattened))
        assert reassemble(d) == compose(CONTENT)


def test_needed_research_takes_its_targets_level_plus_one():
    """An NR's level is not derived from its own `NR-<n>` number, which carries no
    position. It is one below the document it is emitted under, under the same cap, in the
    file and in the composed Atlas alike.
    """
    def nr_levels(heads):
        out, last = {}, None
        for level, doc_no in heads:
            if doc_no.startswith("NR-"):
                out[doc_no] = (level, last)
            else:
                last = level
        return out

    in_files = {}
    for heads in _split_headings().values():
        in_files.update(nr_levels(heads))
    assert in_files, "no NR documents found — this test would be vacuous"
    for doc_no, (level, target_level) in in_files.items():
        assert level == min(target_level + 1, MAX_HEADING_LEVEL), doc_no

    absolute = dict((dn, lv) for lv, dn in _headings(compose(CONTENT)))
    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        restored = nr_levels(_headings(reassemble(d)))
    assert set(restored) == set(in_files)
    for doc_no, (level, target_level) in restored.items():
        assert level == min(target_level + 1, MAX_HEADING_LEVEL) == absolute[doc_no], doc_no


def test_scenario_variation_levels_survive_the_round_trip():
    """A Scenario Variation's doc number ends in a non-integer `var` segment rather than
    naming a further level, so it sits one below its Scenario and not one below its own
    segment count.
    """
    absolute = dict((dn, lv) for lv, dn in _headings(compose(CONTENT)))
    variations = [dn for dn in absolute if dn.split(".")[-1].startswith("var")]
    assert variations, "no Scenario Variations found — this test would be vacuous"

    for dn in variations:
        scenario = ".".join(dn.split(".")[:-1])
        assert absolute[dn] == min(absolute[scenario] + 1, MAX_HEADING_LEVEL)

    in_files = {dn: lv for heads in _split_headings().values() for lv, dn in heads}
    for dn in variations:
        scenario = ".".join(dn.split(".")[:-1])
        assert in_files[dn] == min(in_files[scenario] + 1, MAX_HEADING_LEVEL)

    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        restored = dict((dn, lv) for lv, dn in _headings(reassemble(d)))
    assert {dn: restored[dn] for dn in variations} == {dn: absolute[dn] for dn in variations}


def test_restore_absolute_levels_leaves_non_heading_lines_alone():
    """Body text that looks like a heading is not one: `HEADING_RE` requires the trailing
    UUID comment. Restoration touches only the lines it matches.
    """
    def heading(doc_no, n):
        return f"# {doc_no} - Name [Core]  <!-- UUID: {str(n) * 8}-1111-1111-1111-111111111111 -->"

    lines = [
        heading("A.6", 1),
        heading("A.6.1", 2),
        heading("A.6.1.1", 3),
        heading("A.6.1.1.1", 4),
        "#### not a document heading",
        "",
        heading("A.6.1.1.1.1", 5),
    ]
    restored = restore_absolute_levels(lines)
    assert restored[4:6] == lines[4:6]
    assert [len(ln.split(" ", 1)[0]) for ln in restored[:4]] == [1, 2, 3, 4]
    assert restored[6].startswith("##### A.6.1.1.1.1 - ")


# ---------------------------------------------------------------------------
# The two invariants
# ---------------------------------------------------------------------------

def test_invariant_1_reassemble_is_byte_identical_to_compose():
    with tempfile.TemporaryDirectory() as d:
        write_split(CONTENT, d)
        assert reassemble(d) == compose(CONTENT)


def test_invariant_2_split_path_decomposes_to_the_same_tree():
    with tempfile.TemporaryDirectory() as d:
        split_dir = os.path.join(d, "split")
        write_split(CONTENT, split_dir)

        base_tree = os.path.join(d, "base")
        c_tree = os.path.join(d, "optionc")

        mono = os.path.join(d, "monolith.md")
        with open(mono, "w", encoding="utf-8") as f:
            f.write(compose(CONTENT))
        decompose(mono, base_tree)

        reasm = os.path.join(d, "reassembled.md")
        with open(reasm, "w", encoding="utf-8") as f:
            f.write(reassemble(split_dir))
        decompose(reasm, c_tree)

        r = subprocess.run(["diff", "-r", base_tree, c_tree],
                           capture_output=True, text=True)
        assert r.returncode == 0, (
            "the Option C split path produced a different tree than the monolith path:\n"
            + "\n".join(r.stdout.splitlines()[:40])
        )


# ---------------------------------------------------------------------------
# Index removal
# ---------------------------------------------------------------------------

def test_no_index_output_is_exactly_the_documents():
    """The 3,851 generated `_index.md` files are not carried into Option C. They exist to
    make the atomized tree navigable on GitHub; under Option C the consolidated files are
    the navigation.

    They are also the bulk of the drift between the tree and the tooling:
    `decompose(compose(content))` differs from `content/` in 1,606 diff lines with them
    and 13 without, and 3 of the 5 remaining differences are directories containing
    nothing but an `_index.md`.

    This asserts the omission is exactly that and nothing else: the same documents, byte
    for byte, with only the generated navigation gone.
    """
    with tempfile.TemporaryDirectory() as d:
        split_dir = os.path.join(d, "split")
        write_split(CONTENT, split_dir)
        mono = os.path.join(d, "m.md")
        with open(mono, "w", encoding="utf-8") as f:
            f.write(reassemble(split_dir))

        with_idx = os.path.join(d, "with")
        without = os.path.join(d, "without")
        decompose(mono, with_idx)
        decompose(mono, without, write_indexes=False)

        assert not [p for _r, _d, fs in os.walk(without) for p in fs if p == "_index.md"]
        r = subprocess.run(["diff", "-r", "-x", "_index.md", with_idx, without],
                           capture_output=True, text=True)
        assert r.returncode == 0, (
            "dropping _index.md changed something other than the index files:\n"
            + "\n".join(r.stdout.splitlines()[:20])
        )
