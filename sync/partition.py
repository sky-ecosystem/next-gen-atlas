#!/usr/bin/env python3
"""Option C: split the composed Atlas into per-Scope and per-Agent-Artifact files.

De-atomization replaces the ~11,300-file `content/` tree with a small set of composed
markdown files. Option C is the variant that keeps each agent artifact in its own file and
breaks Sky Core out by Scope, rather than collapsing Sky Core into one file (Option B).
The operational reason is edit-overlap detection: `prepare-proposal` decides whether two
in-flight edits conflict by intersecting changed paths, and under B that degenerates to
"are these both Sky Core?" — true for nearly every edit. C gives it seven buckets instead
of one.

Not a tree walker
-----------------
It is not a fifth tree walker. There are already four independent implementations of the
`content/` walk across four deploy surfaces, and adding another would make five things
that must agree. This module consumes `compose.compose_segments()` — the same walk,
the same order, the same heading-level computation — and only decides *which output file*
each already-composed document belongs to.

The partition
-------------
Seven files for the Sky Core Atlas, one per Scope, each holding that Scope's whole subtree:

    A.0  Atlas Preamble          A.3  The Stability Scope
    A.1  The Governance Scope    A.4  The Protocol Scope
    A.2  The Support Scope       A.5  The Accessibility Scope
                                 A.6  The Agent Scope  (spine — see below)

plus one file per Agent: currently 8 Prime Agents (`A.6.1.1.1` … `A.6.1.1.8`) and 3
Executor Agents (`A.6.1.2.1` … `A.6.1.2.3`), for 18 files. No agent is named in this
module; agents are identified by position, so onboarding one requires no code change.

The Agent Scope spine belongs to the Scope, not to any agent. `A.6`, `A.6.1` and every
`List Of … Agent Artifacts` Section (`A.6.1.1`, `A.6.1.2`, and any type added later) take
the `A.6` bucket, exactly as `A.1`'s own document takes the `A.1` bucket. A rule that
omits them drops those documents while every other document still lands somewhere, so the
total document count reconciles and no count-based check detects the loss.

Buckets need not be contiguous, and `A.6` is not. Emit order inside the Agent Scope is
`A.6, A.6.1, A.6.1.1, [Primes], A.6.1.2, [Executors]`, so the `A.6` bucket is two runs
with the Prime Agent files between them. Reassembly orders documents (`order_documents`)
rather than concatenating files in bucket order, so the partition follows the Atlas's
structure and contiguity is not required. This matters as the Atlas grows: each new agent
type adds another `List Of …` Section emitted after the previous type's agents, which
would fragment `A.6` into one further run per type.

There is no manifest: no generated file for edit branches to conflict on, nothing to go
stale, and nothing to configure when an agent is onboarded. `split()` verifies end to end
that the partition it produced reassembles byte-identically.

Placement is docNo-derived (`decompose.Document.folder_path_segments`). Incorrect order
would not misplace documents; it would reorder documents within a file silently, which is
why order is asserted rather than assumed.

Needed Research documents carry no independent position. `compose` emits each one
immediately after its placement target, so an NR inherits that document's bucket
(`bucket_for` returns None, meaning "same as previous") and travels inside that document's
`Block` at reassembly rather than being sorted on its own.

Heading levels are file-relative. Each file's root document is `#`, its children `##`, and
so on, so every file opens at the top of the heading range instead of at the depth its
subtree happens to sit at in the whole Atlas. The composed Atlas's absolute levels are
re-derived at reassembly by `restore_absolute_levels`, so nothing depends on the hashes a
file stores.

Usage:
    python partition.py --input content/ --output-dir split/
    python partition.py --input content/ --output-dir split/ --report
"""

from __future__ import annotations

import argparse

import os
import re
import sys
from dataclasses import dataclass

from compose import compose_segments
from decompose import HEADING_RE

# The Agent Scope bucket — holds the whole spine above the individual agents: `A.6`
# itself, the `A.6.1` Agent Artifacts Article, and every `List Of … Agent Artifacts`
# Section beneath it (`A.6.1.1` Prime, `A.6.1.2` Executor, and any type added later).
AGENT_SCOPE_BUCKET = "A.6"

# Every `List Of … Agent Artifacts` Section is a child of this Article, so an individual
# agent is exactly a grandchild of it: `A.6.1.<type>.<agent>`, five segments.
AGENT_ARTIFACTS_ARTICLE = "A.6.1"
AGENT_DOC_NO_SEGMENTS = 5


def bucket_for(doc_no: str) -> str | None:
    """Which output file this document belongs to. None means 'inherit from previous'.

    None is returned only for Needed Research, which compose emits inline under its
    placement target and which therefore has no position of its own.

    The layout is seven Sky Core files (`A.0`–`A.6`), each holding that Scope's whole
    subtree, plus one file per agent.

    An agent is identified by position, not by name. Every `List Of … Agent Artifacts`
    Section is a child of the `A.6.1` Agent Artifacts Article, so an individual agent is
    exactly a grandchild of it — `A.6.1.<type>.<agent>` — and it takes its whole subtree
    with it. Everything at or above that line stays in the `A.6` file: the Scope document,
    the Article, and each `List Of …` Section itself.

    No agent and no agent type is enumerated here. Expressing the rule as a depth rather
    than as a set of doc numbers means a ninth Prime (`A.6.1.1.9`), a fourth Executor
    (`A.6.1.2.4`) and an entirely new agent type (`A.6.1.3 - List Of … Agent Artifacts`,
    whose Section stays in the `A.6` file while each of its children gets a file) all work
    with no code change and nothing to configure.

    `A.6.1.2` belongs in the `A.6` file. It and `A.6.1.1` are both Sections and
    structurally identical siblings. Grouping it with the spine splits the `A.6` bucket
    into two runs, because emit order is `A.6, A.6.1, A.6.1.1, [Primes], A.6.1.2,
    [Executors]`; that is expressible because reassembly orders documents rather than
    buckets. See `order_documents`.
    """
    if doc_no.startswith("NR-"):
        return None

    parts = doc_no.split(".")
    if not parts or parts[0] != "A":
        return "misc"
    if len(parts) == 1:
        return "A"

    if parts[1] != "6":
        return f"A.{parts[1]}"

    # Inside the Agent Scope: an individual agent is a grandchild of the Agent Artifacts
    # Article, and carries its subtree. Everything shallower is Agent Scope spine.
    if (len(parts) >= AGENT_DOC_NO_SEGMENTS
            and ".".join(parts[:3]) == AGENT_ARTIFACTS_ARTICLE):
        return ".".join(parts[:AGENT_DOC_NO_SEGMENTS])

    return AGENT_SCOPE_BUCKET


def order_key(bucket: str) -> tuple[int, ...]:
    """Sort key listing bucket files in the order their root document appears.

    This is presentational only. Reassembly does not depend on it: `order_documents`
    orders documents and is indifferent to the order the files arrive in. What this
    provides is a stable, human-sensible listing order for `--report` and for
    `write_split`'s returned `order`.

    Filename sorting is not a substitute, even for display. It agrees today and diverges
    once a tenth agent exists: lexicographically `A.6.1.1.10` sorts between `A.6.1.1.1`
    and `A.6.1.1.2`.
    """
    return tuple(int(s) for s in bucket.split(".")[1:])


# ---------------------------------------------------------------------------
# Document order
# ---------------------------------------------------------------------------
#
# Reassembly orders documents, not buckets. Ordering by bucket would require every bucket
# to occupy one contiguous run of the emit order, which the Atlas's structure does not
# provide: `A.6.1.2 - List Of Executor Agent Artifacts` is a Section grouped with the
# `A.6` spine, and the Prime Agent files sit between the spine's two runs.
#
# The fragmentation grows with the Atlas. Each new agent type adds another
# `List Of … Agent Artifacts` Section emitted after the previous type's agents, so the
# `A.6` bucket gains one further run per type: two runs today, three with a third type,
# and so on.
#
# With order carried by the documents themselves, contiguity is irrelevant and any
# partition is expressible.


def canonical_sort_key(doc_no: str, real_doc_nos) -> tuple:
    """Compose's emit position for a numbered document, derived from its doc number alone.

    Naive doc-number sorting is wrong in 410 places on today's Atlas. Compose emits a
    parent's real children before any subtree rooted at a phantom extension folder — the
    `0/` directories (e.g. `A/1/4/5/0/4/`) that carry no `document.md` and exist only to
    give Action Tenets and Annotations the right heading depth. So `A.1.1.1` legitimately
    precedes `A.1.1.0.3.1`, which ascending doc-number order gets backwards.

    This reproduces `compose._child_sort_key` exactly, but from doc numbers instead of the
    filesystem: a doc number segment is phantom precisely when no document claims that
    prefix, and `real_doc_nos` is the set of doc numbers actually present. Per segment the
    key is (rank, value) with rank 0 = real child, 1 = phantom, 2 = the non-integer `var1`
    Scenario Variation folder — the same three buckets, in the same order.

    A parent sorts before its own children for free: its key is a prefix of theirs, and a
    shorter tuple compares less.

    `split()` re-checks the whole stream end to end on every call, so any disagreement
    between this key and compose surfaces at write time.
    """
    parts = doc_no.split(".")
    key = []
    for i in range(1, len(parts)):
        seg = parts[i]
        if seg.isdigit():
            prefix = ".".join(parts[:i + 1])
            key.append((0 if prefix in real_doc_nos else 1, int(seg), ""))
        else:
            # `var1` — the only non-integer segment in the Atlas, sole child of a Scenario.
            key.append((2, 0, seg))
    return tuple(key)


# ---------------------------------------------------------------------------
# Heading levels
# ---------------------------------------------------------------------------
#
# The same headings carry two levels. In the composed Atlas the level is absolute: a Scope
# is `#` and everything below it counts from there. In a bucket file the level is relative
# to that file's own root document, which is `#`, its children `##`, and so on. Both cap at
# six, the deepest level markdown has.
#
# Neither level is ever read out of a heading line's hashes. The hash count is lossy —
# 10,194 of the Atlas's 11,335 documents sit at the cap, and 10,254 doc numbers have more
# than six segments — so the hashes cannot tell a document at depth 6 from one at depth 17,
# and subtracting a file's root level from them would flatten every capped document onto
# the wrong level. Depth is carried by the doc number, which every heading line contains,
# and both levels are computed from it.

MAX_HEADING_LEVEL = 6

_HASHES_RE = re.compile(r"^#+")


def structural_depth(doc_no: str, real_doc_nos) -> int:
    """How many documents sit above this one.

    Segment count is not depth. A segment can be a phantom extension folder — the `0`
    segments (e.g. `A.1.4.5.0.4`) that hold no document and exist only to give Action
    Tenets and Annotations the right heading depth — and the leading `A` is phantom too,
    since no document claims it. An ancestor counts precisely when some document claims
    that prefix, the same real/phantom test `canonical_sort_key` applies.

    This reproduces `compose.compute_heading_levels`, which counts ancestor folders holding
    a `document.md`, from doc numbers instead of the filesystem. A folder holds a
    `document.md` exactly when its doc number is claimed, so the two agree everywhere.
    """
    parts = doc_no.split(".")
    return sum(1 for i in range(1, len(parts))
               if ".".join(parts[:i]) in real_doc_nos)


def set_heading_level(line: str, level: int) -> str:
    """Rewrite a heading line's hashes to `level`, leaving the rest of the line untouched."""
    return _HASHES_RE.sub("#" * level, line, count=1)


def restore_absolute_levels(lines: list[str]) -> list[str]:
    """Give every heading in a reassembled stream its level in the composed Atlas.

    Bucket files store levels relative to their own root document, so their hashes are not
    the composed Atlas's hashes. The absolute level is re-derived rather than adjusted:
    `min(structural_depth + 1, 6)` over the whole document set, which is what compose
    computes from the tree. Re-deriving is what makes the cap come out right — a document
    at depth 17 is `######` in the composed Atlas whatever its file stored.

    Needed Research has no position of its own and takes its target's level plus one, under
    the same cap, matching compose. Its target is the numbered document it follows, which
    is where compose emits it and where `Block` keeps it.
    """
    heads = [(i, m) for i, line in enumerate(lines) if (m := HEADING_RE.match(line))]
    real_doc_nos = {m.group(2) for _, m in heads if not m.group(2).startswith("NR-")}

    out = list(lines)
    previous = 0
    for i, m in heads:
        doc_no = m.group(2)
        if doc_no.startswith("NR-"):
            level = min(previous + 1, MAX_HEADING_LEVEL)
        else:
            level = min(structural_depth(doc_no, real_doc_nos) + 1, MAX_HEADING_LEVEL)
            previous = level
        out[i] = set_heading_level(lines[i], level)
    return out


@dataclass
class Block:
    """One numbered document plus any Needed Research emitted under it.

    This is how NR adjacency survives document-level sorting. A Needed Research document
    has no position of its own: its doc number is `NR-<n>`, drawn from a flat namespace
    with no relationship to where it sits, and post-consolidation its target is defined by
    its position (`decompose` derives `targets[0]` as the most recently seen numbered
    document). An NR therefore cannot be given an independent sort key; sorting NRs as
    documents would scatter them and retarget every one.

    The sort unit is the block, anchored by its numbered document, with trailing NRs
    carried along inside it. NRs are never compared, never sorted, and never separated
    from the document they were emitted under.
    """
    doc_no: str          # the numbered document anchoring this block
    source: str          # which bucket/file it came from
    index: int           # position within that source, for the order-preservation check
    lines: list[str]


def split_into_blocks(source: str, lines: list[str]) -> list[Block]:
    """Cut one file's lines into blocks at Atlas document headings.

    Boundaries come from `decompose.HEADING_RE`, the same regex that turns a composed
    stream back into documents, so there is a single definition of a document boundary
    rather than two that could drift apart. It also carries the established behaviour on
    body text that superficially looks like a heading: a plain `#` line does not match,
    because the regex requires the trailing `<!-- UUID: … -->` comment.
    """
    heads = [(i, m.group(2)) for i, line in enumerate(lines)
             if (m := HEADING_RE.match(line))]
    if not heads:
        raise ValueError(f"{source!r} contains no Atlas document headings")
    if heads[0][0] != 0:
        raise ValueError(
            f"{source!r} has {heads[0][0]} line(s) before its first document heading. "
            "Bucket files must begin with a heading, or that text belongs to no document "
            "and would be silently dropped at reassembly."
        )
    if heads[0][1].startswith("NR-"):
        raise ValueError(
            f"{source!r} begins with Needed Research document {heads[0][1]}, which has no "
            "numbered document in this file to travel with. An NR must follow its "
            "placement target — see Block."
        )

    starts = [(i, dn) for i, dn in heads if not dn.startswith("NR-")]
    blocks = []
    for k, (start, doc_no) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        blocks.append(Block(doc_no, source, k, lines[start:end]))
    return blocks


def order_documents(lines_by_source: dict[str, list[str]]) -> list[str]:
    """Merge split files into the single composed line stream, ordered by document.

    This is reassembly's whole algorithm. It does not depend on the order the files are
    given in, their names, their count, or any stored manifest. Order comes from the
    documents themselves, so a new agent, a new agent type, or an entirely different
    partition all reassemble correctly with no configuration anywhere.
    """
    blocks: list[Block] = []
    for source in sorted(lines_by_source):
        blocks.extend(split_into_blocks(source, lines_by_source[source]))

    origin: dict[str, str] = {}
    for b in blocks:
        if b.doc_no in origin:
            raise ValueError(
                f"document {b.doc_no} appears in both {origin[b.doc_no]!r} and "
                f"{b.source!r} — a document must live in exactly one file."
            )
        origin[b.doc_no] = b.source

    real = set(origin)
    ordered = sorted(blocks, key=lambda b: canonical_sort_key(b.doc_no, real))
    _assert_source_order_preserved(ordered)
    return [line for b in ordered for line in b.lines]


def _assert_source_order_preserved(ordered: list[Block]) -> None:
    """Check that the derived order never reorders documents within a single file.

    Within a file the document order is compose's own emit order, frozen into the line
    order at write time, and needs no deriving. `canonical_sort_key` is only genuinely
    needed to interleave different files, but a global sort re-derives the within-file
    order too, and a rule that disagreed with compose anywhere would reorder documents
    silently.

    The sort may interleave files freely, but it must never move a document backwards past
    another from the same file. Any disagreement between the derived rule and compose then
    fails at the exact document where they diverge.
    """
    last: dict[str, int] = {}
    for b in ordered:
        prev = last.get(b.source, -1)
        if b.index <= prev:
            raise ValueError(
                f"document ordering moved {b.doc_no} backwards within {b.source!r} "
                f"(position {b.index} after position {prev}). Within a file the order is "
                "compose's own emit order and is authoritative; the derived key must "
                "never reorder it. This means canonical_sort_key and compose disagree."
            )
        last[b.source] = b.index


_SLUG_STRIP = re.compile(r"[^A-Za-z0-9]+")


def _slug(name: str) -> str:
    return _SLUG_STRIP.sub("-", name).strip("-") or "untitled"


def filename_for(bucket: str, name: str) -> str:
    """Stable, human-navigable filename. The docNo prefix keeps sort order meaningful."""
    return f"{bucket} - {_slug(name)}.md"


def split(content_root: str) -> tuple[dict[str, list[str]], list[dict], dict[str, str]]:
    """Partition the composed Atlas.

    Headings are rewritten to levels relative to each file's root document, so every file
    opens at `#`. See the heading-level section above; `restore_absolute_levels` puts the
    composed Atlas's levels back at reassembly.

    Returns (lines_by_bucket, run_list, name_by_bucket) where run_list is the ordered
    sequence of (bucket, docs) runs describing the global emit order.
    """
    segments = compose_segments(content_root)
    real_doc_nos = {doc.doc_no for doc, _ in segments
                    if not doc.doc_no.startswith("NR-")}

    lines_by_bucket: dict[str, list[str]] = {}
    name_by_bucket: dict[str, str] = {}
    runs: list[dict] = []
    current: str | None = None
    # Each file's root document is its first document, and every other document in the file
    # is below it, so its depth is what the file's levels count from.
    root_depth: dict[str, int] = {}
    previous_level = 0

    for doc, lines in segments:
        bucket = bucket_for(doc.doc_no)
        if bucket is None:
            if current is None:
                raise ValueError(
                    f"NR document {doc.doc_no} was emitted before any bucketed document — "
                    "it has no target to inherit a bucket from."
                )
            bucket = current

        # The document whose docNo *is* the bucket name supplies the file's title.
        if doc.doc_no == bucket:
            name_by_bucket[bucket] = doc.name

        if doc.doc_no.startswith("NR-"):
            level = min(previous_level + 1, MAX_HEADING_LEVEL)
        else:
            depth = structural_depth(doc.doc_no, real_doc_nos)
            base = root_depth.setdefault(bucket, depth)
            if depth < base:
                raise ValueError(
                    f"document {doc.doc_no} sits above the root of its own file "
                    f"(depth {depth} against root depth {base} for bucket {bucket!r}). "
                    "A file's first document must be the shallowest one in it, or the "
                    "file cannot start at `# `."
                )
            level = min(depth - base + 1, MAX_HEADING_LEVEL)
            previous_level = level

        lines = [set_heading_level(lines[0], level)] + lines[1:]
        lines_by_bucket.setdefault(bucket, []).extend(lines)

        # `lines` is what reassembly slices on; `docs` is the per-run document count used
        # by `--report` and by the total-document cross-check.
        if runs and runs[-1]["bucket"] == bucket:
            runs[-1]["docs"] += 1
            runs[-1]["lines"] += len(lines)
        else:
            runs.append({"bucket": bucket, "docs": 1, "lines": len(lines)})
        current = bucket

    _assert_partition_reassembles(segments, lines_by_bucket)
    return lines_by_bucket, runs, name_by_bucket


def _assert_partition_reassembles(segments, lines_by_bucket: dict[str, list[str]]) -> None:
    """Check that this partition reassembles to the composed Atlas byte for byte.

    The check is end to end: partition the composed stream, put it back together the way
    `decompose_multi.reassemble` will — same ordering, same level restoration — and require
    the result to equal what compose emitted. Any partition that survives is safe; any that
    does not fails here, at write time, naming the first document that moved, rather than
    silently reordering documents.

    Because the comparison is byte-exact and covers the heading lines, it also holds the
    relative levels written into the files to the one thing asked of them: that the
    absolute levels can be recovered from the files alone.

    Requiring instead that every bucket be contiguous in emit order is a sufficient but
    stricter condition, and rejects partitions that lose no information — including the
    one that groups `A.6.1.2` with the `A.6` spine.

    This runs inside `split()` rather than `write_split()` so that every caller is covered,
    including `migrate_branch` and the tests.
    """
    expected = [line for _doc, lines in segments for line in lines]
    got = restore_absolute_levels(order_documents(lines_by_bucket))
    if got == expected:
        return
    where = next((i for i, (a, b) in enumerate(zip(got, expected)) if a != b),
                 min(len(got), len(expected)))
    raise ValueError(
        "this partition does not reassemble to the composed Atlas: reassembly and compose "
        f"first differ at line {where} ({len(got):,} lines vs {len(expected):,} expected).\n"
        f"  reassembled: {got[where] if where < len(got) else '<end of stream>'!r}\n"
        f"  compose:     {expected[where] if where < len(expected) else '<end of stream>'!r}\n"
        "Document order is derived by canonical_sort_key; a mismatch means the partition "
        "separated documents whose relative order that key cannot reproduce."
    )


FILENAME_RE = re.compile(r"^(A(?:\.\d+)*) - .*\.md$")


def bucket_from_filename(fname: str) -> str | None:
    """Recover a bucket's doc number from its filename, or None if not a bucket file."""
    m = FILENAME_RE.match(fname)
    return m.group(1) if m else None


def write_split(content_root: str, output_dir: str) -> dict:
    """Write the split files. No manifest is written; order is derived per document."""
    lines_by_bucket, runs, name_by_bucket = split(content_root)

    # Buckets may interleave, and `A.6` does: the Prime Agent files sit between its two
    # runs, which is what lets the Executor Agent list live in the Agent Scope file.
    # `split()` has already checked the property that matters — that this exact partition
    # reassembles byte-identically — via `_assert_partition_reassembles`. Do not add a
    # contiguity check here; it would reject that layout.

    os.makedirs(output_dir, exist_ok=True)
    files = {}
    written: dict[str, str] = {}
    for bucket, lines in lines_by_bucket.items():
        fname = filename_for(bucket, name_by_bucket.get(bucket, bucket))
        if fname in written:
            raise ValueError(
                f"buckets {written[fname]!r} and {bucket!r} both want the filename "
                f"{fname!r}; one would overwrite the other."
            )
        written[fname] = bucket
        files[bucket] = fname
        with open(os.path.join(output_dir, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    return {
        "files": files,
        "order": sorted(files, key=order_key),
        "total_docs": sum(r["docs"] for r in runs),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Split composed Atlas into Option C files.")
    ap.add_argument("--input", required=True, help="content/ directory")
    ap.add_argument("--output-dir", required=True, help="directory to write split files into")
    ap.add_argument("--report", action="store_true", help="print a per-file size report")
    args = ap.parse_args()

    result = write_split(args.input, args.output_dir)
    n = len(result["files"])

    if args.report:
        # Listing order only, by each file's root document. Reassembly does not depend
        # on it — see `order_key`.
        print(f"{'bytes':>10}  file  (by root document)")
        for bucket in result["order"]:
            fname = result["files"][bucket]
            size = os.path.getsize(os.path.join(args.output_dir, fname))
            print(f"{size:>10,}  {fname}")
        print(f"{'':>10}  -- {n} files, {result['total_docs']:,} documents, no manifest")
    else:
        print(f"Wrote {n} files to {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
