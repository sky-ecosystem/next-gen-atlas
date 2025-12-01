"""Generate and add UUIDs for newly added documents.

Creates backup of original file before making changes.
"""

import re
import shutil
import uuid
from pathlib import Path

MARKDOWN_FILE = Path("Sky Atlas/Sky Atlas.md")


HEADER_RE = re.compile(r"^\s*#+\s+.*")
UUID_COMMENT_RE = re.compile(r"<!--\s*UUID: [0-9a-fA-F-]+\s*-->")


def is_header(line: str) -> bool:
    """Check if a line is a markdown header.

    Returns:
        True if the line starts with one or more '#' characters followed by a space.

    """
    return HEADER_RE.match(line) is not None


def has_uuid_comment(line: str) -> bool:
    """Check if a line contains a correctly formatted UUID.

    Returns:
        True if the line contains a UUID comment.

    """
    return UUID_COMMENT_RE.match(line) is not None


def process_markdown(path: Path) -> None:
    """Process a markdown file to add UUIDs to headers that do not contain them.

    Raises:
        FileNotFoundError: If the specified markdown file does not exist.

    """
    if not path.exists():
        msg = f"Markdown file path not found: {path}"
        raise FileNotFoundError(msg)

    headers_tagged = 0

    # Backup Atlas and temp paths
    backup_path = path.with_suffix(path.suffix + ".bak")
    tmp_path = path.with_suffix(path.suffix + ".tmp")

    # Create backup
    shutil.copy2(path, backup_path)
    print(f"Backup created at: {backup_path}")

    with (
        path.open("r", encoding="utf-8") as infile,
        tmp_path.open("w", encoding="utf-8") as outfile,
    ):
        for line in infile:
            original_line = line
            no_nl = line.rstrip("\n")
            trimmed = no_nl.rstrip()

            if is_header(trimmed) and trimmed.endswith("]") and not has_uuid_comment(trimmed):
                new_id = uuid.uuid4()
                new_line = f"{trimmed}  <!-- UUID: {new_id} -->\n"
                outfile.write(new_line)
                headers_tagged += 1
            else:
                outfile.write(original_line)

    print(f"Done. Headers tagged with UUIDs: {headers_tagged}")

    # Replace original file with temp file
    tmp_path.replace(path)

    print(f"Updated {path}. Headers tagged with UUIDs: {headers_tagged}")


def main() -> None:
    """Execute the program to process the markdown file."""
    process_markdown(MARKDOWN_FILE)


if __name__ == "__main__":
    main()
