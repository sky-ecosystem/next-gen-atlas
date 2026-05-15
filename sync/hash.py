"""Compute the SHA3-256 hash of a file.

Library use:
    from sync.hash import hash_file
    digest = hash_file(Path("Sky Atlas/Sky Atlas.md"))

CLI use:
    python sync/hash.py "Sky Atlas/Sky Atlas.md"
    python sync/hash.py --algorithm sha256 some_file.bin
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def hash_file(path: Path, algorithm: str = "sha3_256") -> str:
    """Return the hex digest of `path` using the named hashlib algorithm."""
    logger.info("Hashing %s with %s", path, algorithm)
    with open(path, "rb") as f:
        digest = hashlib.file_digest(f, algorithm)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute a cryptographic hash of a file."
    )
    parser.add_argument("path", type=Path, help="File to hash")
    parser.add_argument(
        "--algorithm",
        default="sha3_256",
        help="hashlib algorithm name (default: sha3_256)",
    )
    parser.add_argument(
        "--log-level",
        default="WARNING",
        help="Logging level (default: WARNING)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=args.log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    print(hash_file(args.path, args.algorithm))
    return 0


if __name__ == "__main__":
    sys.exit(main())
