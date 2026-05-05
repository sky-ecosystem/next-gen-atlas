#!/usr/bin/env python3
"""Decompose the monolithic Sky Atlas markdown file into the folder-per-document format.

Each document in the Atlas is a heading line matching this pattern:
    #{1,6} {docNo} - {name} [{type}]  <!-- UUID: {uuid} -->

The script parses every document, extracts metadata, and writes individual
document.md files (with YAML frontmatter) and _index.md files into a
folder-per-document tree.

Usage:
    python decompose.py --input "path/to/Sky Atlas.md" --output output_dir
    python decompose.py --input "path/to/Sky Atlas.md" --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Regex for parsing Atlas heading lines
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(
    r"^(#{1,6})\s+"          # heading level (group 1)
    r"(\S+)"                 # doc number (group 2)
    r"\s+-\s+"               # separator " - "
    r"(.+?)"                 # name (group 3), non-greedy
    r"\s+\[([^\]]+)\]"       # type in brackets (group 4)
    r"\s+<!--\s*UUID:\s*"    # UUID comment start
    r"([0-9a-f-]+)"          # UUID (group 5)
    r"\s*-->"                # UUID comment end
)


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Document:
    """Represents a single Atlas document."""
    doc_no: str
    name: str
    doc_type: str
    uuid: str
    heading_level: int
    content: str = ""
    line_number: int = 0
    # For Needed Research documents: list of UUIDs of attached Target Documents.
    # Per Atlas Type Specification A.1.2.2.2.30, NRs are standalone (their identifier
    # is not derived from the Target Document tree position) and may attach to
    # multiple Target Documents. Today's decompose captures the placement-target
    # (the most-recently-emitted non-NR document at NR encounter time) at index 0.
    # Empty for non-NR documents.
    targets: list[str] = field(default_factory=list)

    @property
    def is_nr(self) -> bool:
        return self.doc_no.startswith("NR-")

    @property
    def segments(self) -> list[str]:
        """Split doc number into segments."""
        if self.is_nr:
            return self.doc_no.split("-")
        return self.doc_no.split(".")

    @property
    def depth(self) -> int:
        """Compute semantic depth from the doc number."""
        if self.is_nr:
            return 2
        segs = self.segments
        # Scope documents (A.N): depth = segments - 1 = 1
        if self.doc_type == "Scope":
            return len(segs) - 1
        # Scenario Variation documents (last segment starts with 'var'):
        # depth = segments - 1
        if segs and segs[-1].startswith("var"):
            return len(segs) - 1
        # All other A.* documents: depth = segment count
        return len(segs)

    @property
    def output_heading_level(self) -> int:
        """Heading level to use in the output document.md."""
        return min(self.depth + 1, 6)

    @property
    def folder_path_segments(self) -> list[str]:
        """Path segments for the folder structure."""
        if self.is_nr:
            # NR-7 -> ['NR', '7']
            parts = self.doc_no.split("-")
            return parts
        # A.6.1.1 -> ['A', '6', '1', '1']
        return self.doc_no.split(".")

    @property
    def child_type(self) -> str:
        """Determine the childType frontmatter value."""
        type_map = {
            "Article": "articles",
            "Active Data": "active_data",
            "Annotation": "annotations",
            "Scenario": "tenets",
            "Scenario Variation": "tenets",
            "Needed Research": "needed_research",
        }
        return type_map.get(self.doc_type, "sections_and_primary_docs")

    @property
    def last_segment(self) -> str:
        """The last segment of the doc number (used as folder name)."""
        return self.folder_path_segments[-1]


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_atlas(text: str) -> list[Document]:
    """Parse the Atlas markdown into a list of Documents.

    Each document's content is the verbatim text between its heading and the
    next heading (or end of file), preserving leading/trailing blank lines so
    that compose can roundtrip back to the original byte stream.

    For Needed Research documents, the placement-target (the UUID of the
    most-recently-encountered non-NR document) is captured into `targets[0]`.
    """
    lines = text.split("\n")
    documents: list[Document] = []
    current_doc: Optional[Document] = None
    content_lines: list[str] = []
    last_non_nr_uuid: Optional[str] = None

    def finalize_doc():
        """Finalize the current document by setting its content."""
        nonlocal current_doc, content_lines
        if current_doc is not None:
            # Preserve content verbatim — no extra-field stripping. Compose
            # relies on byte-exact body to roundtrip.
            current_doc.content = "\n".join(content_lines)
            documents.append(current_doc)
        current_doc = None
        content_lines = []

    for i, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line)
        if m:
            finalize_doc()
            hashes, doc_no, name, doc_type, uuid = m.groups()
            current_doc = Document(
                doc_no=doc_no,
                name=name,
                doc_type=doc_type,
                uuid=uuid,
                heading_level=len(hashes),
                line_number=i,
            )
            if doc_no.startswith("NR-"):
                if last_non_nr_uuid is not None:
                    current_doc.targets = [last_non_nr_uuid]
            else:
                last_non_nr_uuid = uuid
            content_lines = []
        elif current_doc is not None:
            content_lines.append(line)

    finalize_doc()
    return documents


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------

def yaml_quote_name(name: str) -> str:
    """Quote the name field for YAML if it contains special characters.

    Returns the name as-is if safe, or wrapped in double quotes with internal
    double quotes escaped using backslash. Only quotes when the name contains
    characters that would actually break YAML block scalar parsing.
    """
    # Characters that require YAML quoting in block scalars
    special_chars = ('"', "'", "&", ":", "#", "{", "}", "[", "]", "!", "|", ">", "%", "@", "`")
    needs_quoting = any(ch in name for ch in special_chars)

    if not needs_quoting:
        return name

    # Escape internal double quotes with backslash
    escaped = name.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def build_frontmatter(doc: Document) -> str:
    """Build YAML frontmatter for a document."""
    name_value = yaml_quote_name(doc.name)
    lines = [
        "---",
        f"id: {doc.uuid}",
        f"docNo: {doc.doc_no}",
        f"name: {name_value}",
        f"type: {doc.doc_type}",
        f"depth: {doc.depth}",
        f"childType: {doc.child_type}",
    ]
    # Needed Research documents carry their attachment relationship explicitly
    # (per A.1.2.2.2.30 — NR identifiers don't encode the Target Document
    # structurally, so the linkage lives here in frontmatter instead).
    if doc.is_nr and doc.targets:
        targets_str = ", ".join(doc.targets)
        lines.append(f"targets: [{targets_str}]")
    lines.append("---")
    return "\n".join(lines)


def build_heading(doc: Document) -> str:
    """Build the heading line for the output document.md."""
    hashes = "#" * doc.output_heading_level
    return f"{hashes} {doc.doc_no} - {doc.name} [{doc.doc_type}]"


def build_document_md(doc: Document) -> str:
    """Build the complete document.md content.

    Layout (each `\\n` is one byte):
        ---
        {frontmatter inner}
        ---
        [blank line — separator between frontmatter and heading]
        {heading}
        {content_lines verbatim, joined with newlines}

    `doc.content` is what `parse_atlas` produced via
    `"\\n".join(content_lines)`. Since Atlas headings are always followed
    by a blank line in source, `content_lines[0] == ""` and therefore
    `doc.content` starts with a leading "\\n". That leading "\\n" is the
    SEPARATOR between content_lines[0] (blank) and content_lines[1] — it
    does NOT also serve as the separator between heading and content. So
    we add an explicit "\\n" between heading and content, producing the
    desired "heading\\n[blank]\\n[first body line]..." structure.

    If a doc has no body (last doc in file with nothing after heading),
    `doc.content` is "" and we emit just the heading with a trailing newline.
    """
    frontmatter = build_frontmatter(doc)
    heading = build_heading(doc)

    if doc.content:
        return f"{frontmatter}\n\n{heading}\n{doc.content}"
    else:
        return f"{frontmatter}\n\n{heading}\n"


def doc_folder_path(doc: Document, output_root: str) -> str:
    """Compute the folder path for a document."""
    return os.path.join(output_root, *doc.folder_path_segments)


# ---------------------------------------------------------------------------
# Index generation
# ---------------------------------------------------------------------------

@dataclass
class IndexEntry:
    """An entry in an _index.md file."""
    doc_no: str
    name: str
    identifier: str  # last path segment


def build_index_md(
    relative_path: str,
    entries: list[IndexEntry],
) -> str:
    """Build an _index.md file."""
    lines = [
        "---",
        "type: index",
        f"path: {relative_path}",
        f"childCount: {len(entries)}",
        "---",
        "",
        "# Contents",
        "",
    ]
    for entry in entries:
        lines.append(f"- [{entry.doc_no} - {entry.name}]({entry.identifier}/document.md)")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Tree building and writing
# ---------------------------------------------------------------------------

def compute_children(documents: list[Document]) -> dict[str, list[IndexEntry]]:
    """Compute child entries for each parent directory.

    Returns a dict mapping parent folder path segments (tuple joined with /)
    to the list of IndexEntry objects that should appear in that directory's
    _index.md.
    """
    children: dict[str, list[IndexEntry]] = {}

    for doc in documents:
        segments = doc.folder_path_segments
        if len(segments) < 2:
            continue

        parent_key = "/".join(segments[:-1])
        entry = IndexEntry(
            doc_no=doc.doc_no,
            name=doc.name,
            identifier=segments[-1],
        )

        if parent_key not in children:
            children[parent_key] = []
        children[parent_key].append(entry)

    return children


def build_top_level_index(
    documents: list[Document],
    output_root: str,
) -> dict[str, str]:
    """Build special top-level index files.

    Returns a dict of relative file paths -> content.
    """
    indexes: dict[str, str] = {}

    # Collect scopes (A.0 through A.6) for content/_index.md and content/A/_index.md
    scopes = [d for d in documents if d.doc_type == "Scope"]
    scopes.sort(key=lambda d: d.segments)

    if scopes:
        # content/_index.md - links use A/{num}/document.md
        scope_entries_top = [
            IndexEntry(doc_no=d.doc_no, name=d.name, identifier=f"A/{d.last_segment}")
            for d in scopes
        ]
        indexes["_index.md"] = build_index_md("content", scope_entries_top)

        # content/A/_index.md - links use {num}/document.md
        scope_entries_a = [
            IndexEntry(doc_no=d.doc_no, name=d.name, identifier=d.last_segment)
            for d in scopes
        ]
        indexes[os.path.join("A", "_index.md")] = build_index_md("content/A", scope_entries_a)

    # Collect NR documents for content/NR/_index.md
    nr_docs = [d for d in documents if d.is_nr]
    nr_docs.sort(key=lambda d: int(d.doc_no.split("-")[1]))

    if nr_docs:
        nr_entries = [
            IndexEntry(doc_no=d.doc_no, name=d.name, identifier=d.last_segment)
            for d in nr_docs
        ]
        indexes[os.path.join("NR", "_index.md")] = build_index_md("content/NR", nr_entries)

    return indexes


def plan_output(
    documents: list[Document],
    output_root: str,
) -> dict[str, str]:
    """Plan all files to write.

    Returns a dict of absolute file paths -> file content. Decompose emits
    one `document.md` per Atlas document, plus `_index.md` navigation files
    per folder (matches the structure in archon-research/next-gen-atlas).
    """
    files: dict[str, str] = {}

    # 1. Write document.md for each document
    for doc in documents:
        folder = doc_folder_path(doc, output_root)
        filepath = os.path.join(folder, "document.md")
        files[filepath] = build_document_md(doc)

    # 2. Compute children for per-folder _index.md files
    children = compute_children(documents)
    for parent_key, entries in children.items():
        segments = parent_key.split("/")
        folder = os.path.join(output_root, *segments)
        filepath = os.path.join(folder, "_index.md")
        relative_path = "content/" + "/".join(segments)
        files[filepath] = build_index_md(relative_path, entries)

    # 3. Special top-level indexes (content/_index.md, content/A/_index.md, content/NR/_index.md)
    top_indexes = build_top_level_index(documents, output_root)
    for rel_path, content in top_indexes.items():
        filepath = os.path.join(output_root, rel_path)
        files[filepath] = content

    return files


def write_files(files: dict[str, str]) -> int:
    """Write all files to disk. Returns count of files written."""
    count = 0
    for filepath, content in files.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
    return count


# ---------------------------------------------------------------------------
# Summary and warnings
# ---------------------------------------------------------------------------

def print_summary(
    documents: list[Document],
    files: dict[str, str],
    written: int,
    dry_run: bool,
):
    """Print a summary of the decomposition."""
    doc_count = len(documents)
    a_docs = sum(1 for d in documents if not d.is_nr)
    nr_docs = sum(1 for d in documents if d.is_nr)
    doc_files = sum(1 for p in files if p.endswith("document.md"))
    index_files = sum(1 for p in files if p.endswith("_index.md"))

    print(f"\n{'=' * 60}")
    print(f"Sky Atlas Decomposition Summary")
    print(f"{'=' * 60}")
    print(f"Documents parsed:      {doc_count}")
    print(f"  A.* documents:       {a_docs}")
    print(f"  NR-* documents:      {nr_docs}")
    print(f"document.md files:     {doc_files}")
    print(f"_index.md files:       {index_files}")
    print(f"Total files:           {len(files)}")

    if dry_run:
        print(f"\n[DRY RUN] No files written.")
    else:
        print(f"\nFiles written:         {written}")

    # Warnings
    uuids = [d.uuid for d in documents]
    unique_uuids = set(uuids)
    if len(uuids) != len(unique_uuids):
        dup_count = len(uuids) - len(unique_uuids)
        print(f"\nWARNING: {dup_count} duplicate UUID(s) found!")

    # Check for duplicate doc numbers
    doc_nos = [d.doc_no for d in documents]
    unique_doc_nos = set(doc_nos)
    if len(doc_nos) != len(unique_doc_nos):
        dup_count = len(doc_nos) - len(unique_doc_nos)
        print(f"WARNING: {dup_count} duplicate document number(s) found!")

    # Type distribution
    type_counts: dict[str, int] = {}
    for d in documents:
        type_counts[d.doc_type] = type_counts.get(d.doc_type, 0) + 1
    print(f"\nDocument types:")
    for t in sorted(type_counts.keys()):
        print(f"  {t}: {type_counts[t]}")

    print(f"{'=' * 60}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def decompose(input_path: str, output_path: str, dry_run: bool = False) -> dict[str, str]:
    """Main decomposition function.

    Args:
        input_path: Path to the Sky Atlas markdown file.
        output_path: Output directory for the decomposed files.
        dry_run: If True, plan but don't write files.

    Returns:
        Dict of file paths to contents (the planned output).
    """
    print(f"Reading: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"Parsing documents...")
    documents = parse_atlas(text)

    if not documents:
        print("ERROR: No documents found!")
        return {}

    print(f"Planning output to: {output_path}")
    files = plan_output(documents, output_path)

    written = 0
    if not dry_run:
        print(f"Writing files...")
        written = write_files(files)

    print_summary(documents, files, written, dry_run)
    return files


def main():
    parser = argparse.ArgumentParser(
        description="Decompose the Sky Atlas markdown into folder-per-document format."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the Sky Atlas markdown file.",
    )
    parser.add_argument(
        "--output",
        default="content/",
        help="Output directory (default: content/).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be done without writing files.",
    )
    args = parser.parse_args()

    decompose(args.input, args.output, args.dry_run)


if __name__ == "__main__":
    main()
