#!/usr/bin/env python3
"""Option C: split the composed Atlas into per-Scope and per-Agent-Artifact files.

De-atomization replaces the ~11,300-file `content/` tree with a small set of composed
markdown files. Option C is the variant that keeps **each agent artifact in its own file**
*and* **breaks Sky Core out by Scope**, rather than collapsing Sky Core into one file
(Option B). The operational reason is edit-overlap detection: `prepare-proposal` decides
whether two in-flight edits conflict by intersecting changed paths, and under B that
degenerates to "are these both Sky Core?" — true for nearly every edit. C gives it seven
buckets instead of one.

WHAT THIS MODULE IS NOT
-----------------------
It is not a fifth tree walker. There are already four independent implementations of the
`content/` walk across four deploy surfaces, and adding another would make five things
that must agree. This module consumes `compose.compose_segments()` — the same walk,
the same order, the same heading-level computation — and only decides *which output file*
each already-composed document belongs to.

THE PARTITION
-------------
Top-level buckets are the Atlas's own top-level structure, one file each:

    A.0  Atlas Preamble          A.3  The Stability Scope
    A.1  The Governance Scope    A.4  The Protocol Scope
    A.2  The Support Scope       A.5  The Accessibility Scope
                                 A.6  The Agent Scope  (spine only — see below)

plus one file per **Prime Agent artifact** — every child of `A.6.1.1` (Spark, Grove, Keel,
Skybase, Obex, Pattern, Osero, Launch Agent 7) — and one for `A.6.1.2`, the Executor list,
which travels with its own children (Amatsu, Ozone, Core Council Executor Agent 1).

⭐ THE AGENT SCOPE SPINE IS NOT INSIDE ANY ARTIFACT, AND MUST NOT BE FANNED INTO ONE.
`A.6` (The Agent Scope), `A.6.1` (Agent Artifacts) and `A.6.1.1` (List Of Prime Agent
Artifacts) are containers belonging to the scope, not to any single Star, and they get the
`A.6` bucket exactly as `A.1`'s own document gets the `A.1` bucket. Adam caught this on
2026-08-10; without it those documents have no home, and — because every *other* document
still lands somewhere — the total document count reconciles anyway. A silent drop that
passes a count check.

⭐⭐ EVERY BUCKET IS CONTIGUOUS IN EMIT ORDER, AND THE PARTITION IS BUILT TO KEEP IT THAT
WAY. That property is what lets the split directory be **self-describing**: reassembly needs
only the order of the buckets, and `order_key` derives it from their doc numbers. There is
no manifest, so there is no generated file for every edit branch to conflict on, nothing to
go stale, and nothing to configure when a new Star is onboarded — which Sky expects to keep
doing. `write_split` asserts contiguity and refuses to write if a future partition change
breaks it, because a non-contiguous bucket cannot be expressed by bucket order alone.

Placement is docNo-derived (`decompose.Document.folder_path_segments`), so getting order
wrong would not misplace documents — it would silently reorder generated `_index.md`
entries across hundreds of files, with nothing raised anywhere. That is why order is
asserted rather than assumed.

Needed Research documents carry no independent position: `compose` emits each NR
immediately after its placement target, so an NR inherits the bucket of the document it
was emitted under (`bucket_for` returns None for them, meaning "same as previous").

Usage:
    python partition.py --input content/ --output-dir split/
    python partition.py --input content/ --output-dir split/ --report
"""

from __future__ import annotations

import argparse

import os
import re
import sys

from compose import compose_segments

# Children of this doc number are individually-filed agent artifacts.
PRIME_ARTIFACT_PARENT = "A.6.1.1"

# The Executor list travels WITH its children as one bucket — see the contiguity note.
EXECUTOR_BUCKET = "A.6.1.2"

# The Agent Scope bucket — holds the spine documents above the artifact lists.
AGENT_SCOPE_BUCKET = "A.6"


def bucket_for(doc_no: str) -> str | None:
    """Which output file this document belongs to. None means 'inherit from previous'.

    None is returned only for Needed Research, which compose emits inline under its
    placement target and which therefore has no position of its own.

    ⭐ WHY `A.6.1.2` IS ITS OWN BUCKET RATHER THAN PART OF THE `A.6` SPINE.
    Emit order inside the Agent Scope is: A.6, A.6.1, A.6.1.1, [Spark] … [Launch Agent 7],
    A.6.1.2, [Amatsu, Ozone, Core Council Executor Agent 1]. Grouping `A.6.1.2` with the
    other three spine documents therefore makes the `A.6` bucket span TWO runs separated by
    every artifact — and a non-contiguous bucket has to store its interleaving somewhere.
    The first version of this module did exactly that, in a `_manifest.json` carrying
    per-run line counts, and it was a mistake twice over: the counts changed on every
    content edit, so every edit branch conflicted with every other on that one file, and
    the integrity check it enabled would have fired on the ordinary act of editing a
    consolidated file — the very workflow this migration exists to enable.

    Splitting the Executor list into its own bucket makes ALL 16 buckets contiguous, at
    which point the only thing reassembly needs is the ORDER OF THE BUCKETS, which
    `order_key` derives. No stored state, nothing to conflict on. Adam asked what the
    manifest was for, 2026-08-10; the honest answer was that it was compensating for a
    partition boundary chosen a document too high.
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

    # Inside the Agent Scope.
    if len(parts) >= 4 and ".".join(parts[:4]) == EXECUTOR_BUCKET:
        return EXECUTOR_BUCKET
    if len(parts) >= 5 and ".".join(parts[:4]) == PRIME_ARTIFACT_PARENT:
        return ".".join(parts[:5])

    # A.6, A.6.1, A.6.1.1 — the spine.
    return AGENT_SCOPE_BUCKET


def order_key(bucket: str) -> tuple[int, ...]:
    """Sort key placing buckets in composed-Atlas order. Deterministic, no stored list.

    Buckets are doc numbers, so their integer-segment tuple IS their position: a prefix
    sorts before its extensions (`A.6` before `A.6.1.1.1`) and segment-wise comparison
    puts `A.6.1.1.8` before `A.6.1.2` because 1 < 2 at the third segment. Verified against
    the real emit order on 2026-08-10.

    ⛔ DO NOT SUBSTITUTE FILENAME SORTING. It agrees today and diverges the moment a tenth
    Star is added: lexicographically `A.6.1.1.10` sorts between `A.6.1.1.1` and
    `A.6.1.1.2`, silently reordering ~2,000 documents with no error anywhere.
    """
    return tuple(int(s) for s in bucket.split(".")[1:])


_SLUG_STRIP = re.compile(r"[^A-Za-z0-9]+")


def _slug(name: str) -> str:
    return _SLUG_STRIP.sub("-", name).strip("-") or "untitled"


def filename_for(bucket: str, name: str) -> str:
    """Stable, human-navigable filename. The docNo prefix keeps sort order meaningful."""
    return f"{bucket} - {_slug(name)}.md"


def split(content_root: str) -> tuple[dict[str, list[str]], list[dict], dict[str, str]]:
    """Partition the composed Atlas.

    Returns (lines_by_bucket, run_list, name_by_bucket) where run_list is the ordered
    sequence of (bucket, docs) runs describing the global emit order.
    """
    segments = compose_segments(content_root)

    lines_by_bucket: dict[str, list[str]] = {}
    name_by_bucket: dict[str, str] = {}
    runs: list[dict] = []
    current: str | None = None

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

        lines_by_bucket.setdefault(bucket, []).extend(lines)

        # `lines` is what reassembly actually slices on; `docs` is the cross-check that
        # catches a file edited out from under the manifest.
        if runs and runs[-1]["bucket"] == bucket:
            runs[-1]["docs"] += 1
            runs[-1]["lines"] += len(lines)
        else:
            runs.append({"bucket": bucket, "docs": 1, "lines": len(lines)})
        current = bucket

    return lines_by_bucket, runs, name_by_bucket


FILENAME_RE = re.compile(r"^(A(?:\.\d+)*) - .*\.md$")


def bucket_from_filename(fname: str) -> str | None:
    """Recover a bucket's doc number from its filename, or None if not a bucket file."""
    m = FILENAME_RE.match(fname)
    return m.group(1) if m else None


def write_split(content_root: str, output_dir: str) -> dict:
    """Write the split files. Deliberately writes NO manifest — see `bucket_for`."""
    lines_by_bucket, runs, name_by_bucket = split(content_root)

    # Contiguity is what makes the partition self-describing. Assert it at write time so
    # a future partition change that reintroduces a split bucket fails HERE, loudly,
    # rather than by silently reordering documents at reassembly.
    if len(runs) != len(lines_by_bucket):
        offenders = [b for b in lines_by_bucket
                     if sum(1 for r in runs if r["bucket"] == b) > 1]
        raise ValueError(
            f"partition produced {len(runs)} runs for {len(lines_by_bucket)} buckets — "
            f"non-contiguous: {offenders}. Reassembly order is derived from bucket doc "
            "numbers alone and cannot express an interleaving; move the boundary."
        )

    os.makedirs(output_dir, exist_ok=True)
    files = {}
    for bucket, lines in lines_by_bucket.items():
        fname = filename_for(bucket, name_by_bucket.get(bucket, bucket))
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
        print(f"{'bytes':>10}  file  (in reassembly order)")
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
