"""Compose the Atlas and hash the result — a one-command integrity check.

⛔ THIS SCRIPT PUBLISHED THE HASH OF AN EMPTY STRING AND EXITED 0.
It called `compose()` directly, which walks for `document.md`. Against the consolidated
layout it finds none, returns "", and this wrote a 0-byte file and printed
a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a -- SHA3-256 of nothing --
as the Atlas digest. `sync/README.md` describes this as "a single-command integrity check:
any change to the decomposed tree changes the digest deterministically." It would have
become a constant: an integrity check reporting "unchanged" no matter what you did.

It also wrote to `Sky Atlas/Sky Atlas.md`, resurrecting the exact path the sync workflow
deletes. Both are fixed by going through `atlas_source`, which composes from either
layout and RAISES on a checkout matching neither rather than returning empty.

Usage:
    python sync/compose_and_hash.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from atlas_source import load_composed
from hash import hash_file

INPUT_DIR = Path("content/")
OUTPUT_FILE = Path("composed-atlas.md")
ALGORITHM = "sha3_256"


def compose_and_hash() -> str:
    """Compose INPUT_DIR into OUTPUT_FILE, then return its hex digest."""
    composed = load_composed(str(INPUT_DIR))
    Path(OUTPUT_FILE.parent).mkdir(exist_ok=True, parents=True)
    OUTPUT_FILE.write_text(composed, encoding="utf-8")

    return hash_file(OUTPUT_FILE, ALGORITHM)


def main() -> None:
    print(compose_and_hash())


if __name__ == "__main__":
    sys.exit(main())
