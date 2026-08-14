#!/usr/bin/env python3
"""Reassemble an Option C split directory and decompose it back to the atomized tree.

Inverse of `partition.py`, and the check that the split is lossless: if the atomized tree
can be reconstructed from the split files byte-for-byte, consolidation destroys no
information.

It adds no parsing of its own. Reassembly merges already-composed line runs, cut at
headings by `decompose.HEADING_RE`, and hands the reconstructed markdown to
`decompose.decompose()` unchanged. Everything deciding where a document lands
(`folder_path_segments`), what its frontmatter says, and how `_index.md` is ordered stays
in one place, so there is no second decomposer to diverge from the first.

Order is derived per document, not stored and not per file. The rule lives in
`partition.canonical_sort_key` / `partition.order_documents`; this module only reads files
and hands them over. Two orderings that do not work: filename sorting, where `A.6.1.1.10`
sorts between `.1` and `.2` once a tenth agent exists; and naive doc-number sorting, which
is wrong in 410 places because compose emits real children before phantom-extension-folder
subtrees.

Usage:
    python decompose_multi.py --input-dir split/ --output content-rt/
    python decompose_multi.py --input-dir split/ --verify-against content/
"""

from __future__ import annotations

import argparse

import os
import subprocess
import sys
import tempfile

from decompose import decompose
from partition import bucket_from_filename, order_documents, restore_absolute_levels


def reassemble(input_dir: str) -> str:
    """Rebuild the single composed markdown stream from the split files.

    There is no manifest and no reliance on file order. Reassembly collects every document
    from every file and orders the documents (`partition.order_documents`). Nothing is
    stored, so nothing goes stale, nothing conflicts when two edit branches touch different
    scopes, and onboarding an agent or an agent type requires no configuration.

    Ordering documents rather than concatenating files in bucket order is what allows a
    bucket to occupy more than one run of the composed stream. Bucket-order reassembly
    cannot express an interleaving, which would force the Executor Agent list into a file
    of its own rather than grouping it with the `A.6` spine, and would add a further run to
    `A.6` for each new agent type.

    The subtle part is Needed Research, which has no position of its own and must stay
    attached to the document it was emitted under; `partition.Block` is where that is
    handled, and the within-file order check in `partition._assert_source_order_preserved`
    is what stops a derived ordering rule from silently disagreeing with compose.

    Heading levels are restored, not carried over. Each file stores levels relative to its
    own root document, and the composed Atlas wants absolute ones, so
    `partition.restore_absolute_levels` re-derives every level from the doc numbers in the
    merged stream. Adjusting the stored hashes instead would not work: nine documents in
    ten are already at the six-hash cap, and a capped hash count no longer says how deep
    its document is.
    """
    names = sorted(os.listdir(input_dir))
    buckets: dict[str, str] = {}
    for fname in names:
        b = bucket_from_filename(fname)
        if b is not None:
            if b in buckets:
                raise ValueError(
                    f"two files claim bucket {b!r}: {buckets[b]!r} and {fname!r}"
                )
            buckets[b] = fname
    if not buckets:
        raise ValueError(f"no Atlas bucket files found in {input_dir!r}")

    lines_by_source: dict[str, list[str]] = {}
    for bucket, fname in buckets.items():
        with open(os.path.join(input_dir, fname), "r", encoding="utf-8") as f:
            lines_by_source[fname] = f.read().split("\n")
    return "\n".join(restore_absolute_levels(order_documents(lines_by_source)))


def main() -> int:
    ap = argparse.ArgumentParser(description="Reassemble + decompose an Option C split.")
    ap.add_argument("--input-dir", required=True, help="split/ directory")
    ap.add_argument("--output", help="output content/ directory")
    ap.add_argument("--verify-against", help="diff the result against this content/ tree")
    ap.add_argument("--emit-markdown", help="write the reassembled markdown here (debug)")
    ap.add_argument("--no-index", action="store_true",
                    help="omit generated _index.md files (Option C target state)")
    args = ap.parse_args()

    text = reassemble(args.input_dir)
    print(f"Reassembled {len(text):,} chars from {args.input_dir}")

    if args.emit_markdown:
        with open(args.emit_markdown, "w", encoding="utf-8") as f:
            f.write(text)

    out_dir = args.output
    tmp_holder = None
    if not out_dir:
        tmp_holder = tempfile.mkdtemp(prefix="atlas-rt-")
        out_dir = os.path.join(tmp_holder, "content")

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
        tf.write(text)
        tmp_md = tf.name
    try:
        decompose(tmp_md, out_dir, write_indexes=not args.no_index)
    finally:
        os.unlink(tmp_md)
    print(f"Decomposed into {out_dir}")

    if args.verify_against:
        r = subprocess.run(
            ["diff", "-r", args.verify_against, out_dir],
            capture_output=True, text=True,
        )
        if r.returncode == 0:
            print(f"ROUNDTRIP OK — {out_dir} is byte-identical to {args.verify_against}")
            return 0
        n = len(r.stdout.splitlines())
        print(f"ROUNDTRIP MISMATCH — {n} diff lines vs {args.verify_against}")
        print("\n".join(r.stdout.splitlines()[:40]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
