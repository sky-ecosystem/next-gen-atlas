"""Compose the Atlas tree into Sky Atlas/Sky Atlas.md and hash the result.

Usage:
    python sync/compose_and_hash.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from compose import compose
from hash import hash_file

INPUT_DIR = Path("content/")
OUTPUT_FILE = Path("Sky Atlas/Sky Atlas.md")
ALGORITHM = "sha3_256"


def compose_and_hash() -> str:
    """Compose INPUT_DIR into OUTPUT_FILE, then return its hex digest."""
    composed = compose(str(INPUT_DIR))
    Path(OUTPUT_FILE.parent).mkdir(exist_ok=True, parents=True)
    OUTPUT_FILE.write_text(composed, encoding="utf-8")

    return hash_file(OUTPUT_FILE, ALGORITHM)


def main() -> None:
    print(compose_and_hash())


if __name__ == "__main__":
    sys.exit(main())
