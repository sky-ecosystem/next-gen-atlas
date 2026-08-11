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

from compose import compose, compose_segments          # noqa: E402
from decompose import HEADING_RE, decompose            # noqa: E402
from decompose_multi import reassemble                 # noqa: E402
from partition import (bucket_for, canonical_sort_key,  # noqa: E402
                       order_documents, order_key, split, write_split)

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
