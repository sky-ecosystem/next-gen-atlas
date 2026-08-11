#!/usr/bin/env python3
"""One entry point that yields the composed Atlas from either layout.

Every consumer — the renderer, the validator, the tar-stream hot path, the portal — needs
the same thing: the composed Atlas markdown for a given checkout. Answering that question
in one place means no consumer needs to know that two layouts exist, and nothing
downstream carries a migration flag.

Alternatives considered and rejected:
  - Dual-mode walkers: five implementations across four deploy cadences, one of them
    pip-installed on developer laptops, would each grow a second code path permanently.
  - Materialising before cutover: a batch job rendering every historical Snapshot into
    storage. Workable, but requires a pre-cutover run, storage, and a retention decision.
    Composing on read requires none of those and imposes no window.

Composing the entire tree measures ~1.9s, and `walk_content_tree` already walks and
composes that tree today, so this is approximately the present cost rather than an
addition to it.

Layout detection is explicit and fails loudly. The pre-existing implicit signal — a walk
that finds no `document.md` returning `[]` — is silently interpreted downstream as a
pre-cutover ref. Post-cutover that same sentinel is what an empty or broken checkout
produces, which makes a genuine failure indistinguishable from an old ref. `detect_layout`
raises on ambiguity rather than guessing, so a truncated checkout surfaces as an error
instead of rendering as an unrecognised layout.
"""

from __future__ import annotations

import os

from compose import compose
from decompose_multi import reassemble
from partition import bucket_from_filename

ATOMIZED = "atomized"
CONSOLIDATED = "consolidated"


class LayoutError(RuntimeError):
    """The checkout matches neither layout, or matches both."""


def detect_layout(root: str) -> str:
    """Classify a checkout's `content/` as atomized or consolidated.

    `root` is the directory that CONTAINS the layout (i.e. the `content/` dir itself for
    the atomized tree, or the split directory for the consolidated one).
    """
    if not os.path.isdir(root):
        raise LayoutError(f"{root!r} is not a directory")

    # Consolidated is identified by its own bucket files. There is deliberately no
    # marker file: a manifest would be generated state that every edit branch conflicts
    # on (see partition.bucket_for), so the layout must be self-evident from the content.
    try:
        buckets = [f for f in os.listdir(root) if bucket_from_filename(f)]
    except OSError as e:
        raise LayoutError(f"cannot read {root!r}: {e}") from e

    # The atomized tree is identified by its root scope document, not by a recursive
    # scan — a recursive "is there any document.md" is both slow and true of a partially
    # written tree.
    has_atom_root = os.path.isfile(os.path.join(root, "A", "0", "document.md"))

    if buckets and has_atom_root:
        raise LayoutError(
            f"{root!r} contains BOTH consolidated bucket files ({len(buckets)}) and an "
            "atomized content tree. That is a half-finished migration — refusing to guess."
        )
    if buckets:
        return CONSOLIDATED
    if has_atom_root:
        return ATOMIZED

    raise LayoutError(
        f"{root!r} matches neither layout: no `A.<n> - <name>.md` bucket files and no "
        "A/0/document.md. An empty or truncated checkout reaches here, and it must NOT "
        "be treated as a pre-cutover ref — which is exactly what the pre-existing "
        "empty-walk-result sentinel silently did."
    )


def load_composed(root: str) -> str:
    """The composed Atlas markdown for this checkout, whichever layout it is in."""
    layout = detect_layout(root)
    return compose(root) if layout == ATOMIZED else reassemble(root)


def main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Compose the Atlas from either layout.")
    ap.add_argument("--input", required=True, help="content/ tree or split/ directory")
    ap.add_argument("--output", help="write composed markdown here (default: stdout len)")
    ap.add_argument("--detect-only", action="store_true", help="print the layout and exit")
    args = ap.parse_args()

    if args.detect_only:
        print(detect_layout(args.input))
        return 0

    text = load_composed(args.input)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {len(text)} chars ({detect_layout(args.input)}) to {args.output}")
    else:
        print(f"{detect_layout(args.input)}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
