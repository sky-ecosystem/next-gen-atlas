#!/usr/bin/env python3
"""Reassemble an Option C split directory and decompose it back to the atomized tree.

Inverse of `partition.py`. This exists to prove the split is LOSSLESS: if the atomized
tree can be reconstructed from the split files byte-for-byte, then consolidation destroys
no information and every downstream consumer can be migrated against a real artifact
rather than a plan.

⭐ IT DELIBERATELY ADDS NO PARSING OF ITS OWN. Reassembly is concatenation in a derived
order, and the reconstructed markdown is handed to the existing, tested
`decompose.decompose()` unchanged. Everything that decides where a document lands
(`folder_path_segments`), what its frontmatter says, and how `_index.md` is ordered stays
in one place. The failure mode this avoids is a second decomposer that agrees with the
first on the current data and diverges on an edge case later.

⛔ ORDER IS DERIVED, NOT STORED — AND FILENAME SORTING IS NOT THE SAME THING.
`partition.order_key` sorts buckets by their doc number as an integer tuple. Lexicographic
filename sorting agrees with it today and breaks silently the moment a tenth Star exists
(`A.6.1.1.10` sorts between `.1` and `.2`), reordering thousands of documents with no
error raised anywhere. Sky expects to onboard more agents, so this is a matter of when.

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
from partition import bucket_from_filename, order_key


def reassemble(input_dir: str) -> str:
    """Rebuild the single composed markdown stream from the split files.

    ⭐ NO MANIFEST, BY DESIGN. Every bucket is contiguous in emit order, so the only
    thing needed is the order of the buckets — and bucket names ARE doc numbers, so
    `partition.order_key` derives it. Nothing is stored, so nothing can go stale, nothing
    conflicts when two edit branches touch different scopes, and onboarding a new Star
    requires no configuration anywhere.

    The messy part of Atlas ordering (real children before phantom extension folders,
    which diverges from naive doc-number sorting in ~410 places) lives entirely WITHIN a
    bucket, already frozen into that file's line order. It never has to be re-derived.
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

    out: list[str] = []
    for bucket in sorted(buckets, key=order_key):
        with open(os.path.join(input_dir, buckets[bucket]), "r", encoding="utf-8") as f:
            out.extend(f.read().split("\n"))
    return "\n".join(out)


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
