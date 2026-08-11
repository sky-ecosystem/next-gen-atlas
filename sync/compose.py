#!/usr/bin/env python3
"""Compose the folder-per-document tree back into the monolithic Sky Atlas markdown.

Inverse of decompose.py. Walks `content/`, parses each document.md, and
reconstructs the linear `Sky Atlas/Sky Atlas.md` byte stream.

Source heading level is computed structurally rather than stored verbatim:
- For non-NR documents: count of ancestor folders that have a `document.md`,
  capped at 6. Phantom extension folders (e.g. `A/1/4/5/0/4/`) carry only
  `_index.md` and don't count, which gives the correct depth for Action
  Tenets, Annotations, Scenarios, and Variations without any path
  restructure.
- For Needed Research documents: their attached Target Document's heading
  level + 1, capped at 6. Target attachment is read from frontmatter
  (`targets: [<UUID>, ...]` — index 0 is the placement anchor; per A.1.2.2.2.30
  NRs may attach to multiple Target Documents but today we encode only the
  source-placement target).

Emit order:
- Depth-first walk of `content/A/`. At each folder: emit the folder's
  document.md (if present), then any NRs whose `targets[0]` matches this
  doc's UUID (sorted by NR number — verified to match source order on
  current data; see decompose change rationale), then recurse into
  children. Children are sorted real-doc-first, then phantom folders.
- `content/NR/` is never walked — every NR is emitted via its target.
  An NR with no resolvable target is appended at end as a sanity fallback,
  with a warning.

Usage:
    python compose.py --input content/ --output "Sky Atlas/Sky Atlas.md"
    python compose.py --input content/ --check "Sky Atlas/Sky Atlas.md"
        # roundtrip check: compose, then diff against the named file.
"""

from __future__ import annotations

import argparse
import difflib
import os
import sys
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ParsedDoc:
    folder_path: tuple[str, ...]   # ('A', '0', '1') for content/A/0/1/document.md
    uuid: str
    doc_no: str
    name: str
    doc_type: str
    depth: int
    child_type: str
    targets: list[str]             # UUIDs of attached Target Documents (NRs only, today)
    content_lines: list[str]       # verbatim from source — split of content_str by "\n"


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def _unquote_yaml_name(s: str) -> str:
    """Inverse of decompose.yaml_quote_name — only handles double-quoted form."""
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        # Decode escaped backslash and double-quote (mirror of yaml_quote_name)
        return s[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    return s


def _parse_targets_value(v: str) -> list[str]:
    """Parse a YAML inline list value like `[uuid1, uuid2]` into a list."""
    v = v.strip()
    if not (v.startswith("[") and v.endswith("]")):
        raise ValueError(f"expected YAML inline list, got {v!r}")
    inner = v[1:-1].strip()
    if not inner:
        return []
    return [t.strip() for t in inner.split(",") if t.strip()]


def parse_document_md(text: str, folder_path: tuple[str, ...]) -> ParsedDoc:
    """Parse a single document.md file.

    Layout (matches build_document_md in decompose.py):
        ---
        {frontmatter inner}
        ---
        [blank line]
        {heading line}
        {content lines, verbatim from source}
    """
    lines = text.split("\n")
    if not lines or lines[0] != "---":
        raise ValueError(f"document.md at {folder_path} does not start with ---")
    try:
        end_fm = lines.index("---", 1)
    except ValueError as e:
        raise ValueError(f"document.md at {folder_path} has unterminated frontmatter") from e

    fm_lines = lines[1:end_fm]
    fm: dict[str, str] = {}
    for fl in fm_lines:
        if ":" not in fl:
            continue
        key, _, val = fl.partition(":")
        fm[key.strip()] = val.strip()

    targets: list[str] = []
    if "targets" in fm:
        targets = _parse_targets_value(fm["targets"])

    # After end_fm: blank line(s), then heading line, then content lines.
    post = lines[end_fm + 1:]
    # Skip leading blank(s) — exactly one is the convention.
    idx = 0
    while idx < len(post) and post[idx] == "":
        idx += 1
    if idx >= len(post):
        # No heading line — doc with empty body? Treat content as empty.
        content_lines: list[str] = []
    else:
        # idx points at the heading line in document.md (which uses
        # min(depth+1, 6) hashes — we don't trust it; we recompute the
        # source heading level from structure).
        content_lines = post[idx + 1:]

    return ParsedDoc(
        folder_path=folder_path,
        uuid=fm["id"],
        doc_no=fm["docNo"],
        name=_unquote_yaml_name(fm["name"]),
        doc_type=fm["type"],
        depth=int(fm["depth"]),
        child_type=fm["childType"],
        targets=targets,
        content_lines=content_lines,
    )


# ---------------------------------------------------------------------------
# Tree discovery
# ---------------------------------------------------------------------------

def find_all_documents(content_root: str) -> list[ParsedDoc]:
    """Walk content_root, parse every document.md, return list of ParsedDocs."""
    docs: list[ParsedDoc] = []
    for root, _dirs, files in os.walk(content_root):
        if "document.md" not in files:
            continue
        rel = os.path.relpath(root, content_root)
        folder_path = tuple(rel.split(os.sep)) if rel != "." else ()
        with open(os.path.join(root, "document.md"), "r", encoding="utf-8") as f:
            text = f.read()
        docs.append(parse_document_md(text, folder_path))
    return docs


# ---------------------------------------------------------------------------
# Heading-level computation
# ---------------------------------------------------------------------------

def compute_heading_levels(
    docs: list[ParsedDoc],
    content_root: str,
) -> dict[str, int]:
    """Compute source heading level for each document, keyed by UUID."""
    by_uuid = {d.uuid: d for d in docs}

    # Cache folder→has_document.md to avoid repeated stat calls.
    has_doc_cache: dict[tuple[str, ...], bool] = {}

    def has_document_md(path: tuple[str, ...]) -> bool:
        if path in has_doc_cache:
            return has_doc_cache[path]
        full = os.path.join(content_root, *path, "document.md") if path else os.path.join(content_root, "document.md")
        result = os.path.isfile(full)
        has_doc_cache[path] = result
        return result

    levels: dict[str, int] = {}

    def level_of(doc: ParsedDoc) -> int:
        if doc.uuid in levels:
            return levels[doc.uuid]
        if doc.doc_no.startswith("NR-"):
            if not doc.targets:
                # Orphan NR — should not happen for valid Atlas, but don't crash.
                lv = 1
            else:
                target = by_uuid.get(doc.targets[0])
                if target is None:
                    lv = 1
                else:
                    lv = min(level_of(target) + 1, 6)
        else:
            # Count ancestor folders that have document.md.
            # folder_path = ('A', '0', '1') means ancestors are ('A',) and ('A', '0').
            count = 0
            for i in range(1, len(doc.folder_path)):
                if has_document_md(doc.folder_path[:i]):
                    count += 1
            lv = min(count + 1, 6)
        levels[doc.uuid] = lv
        return lv

    for d in docs:
        level_of(d)
    return levels


# ---------------------------------------------------------------------------
# Heading line construction
# ---------------------------------------------------------------------------

def build_heading_line(doc: ParsedDoc, level: int) -> str:
    """Reconstruct a source heading line: `# A.0 - Name [Type]  <!-- UUID: ... -->`."""
    return (
        f"{'#' * level} "
        f"{doc.doc_no} - {doc.name} [{doc.doc_type}]"
        f"  <!-- UUID: {doc.uuid} -->"
    )


# ---------------------------------------------------------------------------
# Sibling sort
# ---------------------------------------------------------------------------

def _child_sort_key(parent_full_path: str, child_name: str) -> tuple:
    """Sort children of a folder so emitted order matches source order.

    Empirical rules from current Atlas (verified across all 3,537 parents):
    - All sibling folder names are integer-named, except `var1` (which only
      appears as a sole child of a Scenario folder).
    - `0` folders, when present, are always phantom (no document.md).
    - Real-doc siblings come before phantom siblings.
    - Within a bucket, integer ascending order.

    Sort key: (bucket, numeric_value, name)
        bucket 0: real-doc with integer name
        bucket 1: phantom (no document.md)
        bucket 2: var1 / non-integer (rare/unique)
    """
    full_child = os.path.join(parent_full_path, child_name)
    has_doc = os.path.isfile(os.path.join(full_child, "document.md"))
    if child_name.isdigit():
        return (0 if has_doc else 1, int(child_name), child_name)
    # var1 (only non-integer in current Atlas) — alone in practice, sort late.
    return (2, 0, child_name)


# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------

def compose_segments(content_root: str) -> list[tuple[ParsedDoc, list[str]]]:
    """Walk content_root, return the emit sequence as (doc, lines) pairs.

    This is the structural core of compose(): the order of the returned list is the
    canonical Atlas document order, and flattening its lines reproduces compose()
    byte-for-byte. Exposed separately so a partitioning consumer (Option C split
    output) can assign each document to an output bucket without reimplementing the
    tree walk — there are already four independent walker implementations in the
    ecosystem and this deliberately does not add a fifth.
    """
    docs = find_all_documents(content_root)
    by_uuid = {d.uuid: d for d in docs}
    by_folder = {d.folder_path: d for d in docs}
    levels = compute_heading_levels(docs, content_root)

    # NRs grouped by placement target, sorted numerically.
    nr_by_target: dict[str, list[ParsedDoc]] = {}
    orphan_nrs: list[ParsedDoc] = []
    for d in docs:
        if not d.doc_no.startswith("NR-"):
            continue
        if d.targets and d.targets[0] in by_uuid:
            nr_by_target.setdefault(d.targets[0], []).append(d)
        else:
            orphan_nrs.append(d)
    for k in nr_by_target:
        nr_by_target[k].sort(key=lambda nr: int(nr.doc_no.split("-")[1]))
    orphan_nrs.sort(key=lambda nr: int(nr.doc_no.split("-")[1]))

    segments: list[tuple[ParsedDoc, list[str]]] = []
    emitted: set[str] = set()

    def emit_doc(d: ParsedDoc) -> None:
        if d.uuid in emitted:
            return  # paranoid guard against accidental cycles
        emitted.add(d.uuid)
        segments.append(
            (d, [build_heading_line(d, levels[d.uuid])] + list(d.content_lines))
        )
        # After emitting, emit any NRs attached to this doc.
        for nr in nr_by_target.get(d.uuid, []):
            emit_doc(nr)

    def visit_folder(folder_path: tuple[str, ...]) -> None:
        full_path = os.path.join(content_root, *folder_path)
        # Emit this folder's doc, if present (and not an NR — NRs come via target lookup).
        d = by_folder.get(folder_path)
        if d is not None and not d.doc_no.startswith("NR-"):
            emit_doc(d)
        # Recurse into children.
        try:
            children = [c for c in os.listdir(full_path)
                        if os.path.isdir(os.path.join(full_path, c))]
        except OSError:
            return
        children.sort(key=lambda c: _child_sort_key(full_path, c))
        for child in children:
            visit_folder(folder_path + (child,))

    # Start: walk content/A/ depth-first. Scopes (A.0, A.1, ..., A.6) are the top docs.
    # content/NR/ is intentionally not walked — NRs are emitted via their targets.
    visit_folder(("A",))

    # Sanity: orphan NRs (no resolvable target) get appended at end with a warning.
    if orphan_nrs:
        sys.stderr.write(
            f"WARNING: {len(orphan_nrs)} NR document(s) have no resolvable "
            f"target — appending at end of output.\n"
        )
        for nr in orphan_nrs:
            emit_doc(nr)

    # Sanity: every doc should have been emitted exactly once.
    not_emitted = [d for d in docs if d.uuid not in emitted]
    if not_emitted:
        sys.stderr.write(
            f"WARNING: {len(not_emitted)} document(s) were not emitted by the tree walk:\n"
        )
        for d in not_emitted[:10]:
            sys.stderr.write(f"  - {d.doc_no} at {d.folder_path}\n")

    return segments


def compose(content_root: str) -> str:
    """Walk content_root, emit reconstructed Sky Atlas markdown."""
    return "\n".join(
        line for _doc, lines in compose_segments(content_root) for line in lines
    )


# ---------------------------------------------------------------------------
# Empty-composition guard
# ---------------------------------------------------------------------------

class EmptyCompositionError(RuntimeError):
    """The composition contains no documents. Refuse to write or publish it."""


def guard_composition(composed: str, doc_count: int, source: str) -> None:
    """Refuse to write or hash a composition containing no documents.

    `find_all_documents` walks for `document.md`. Pointed at a consolidated `content/` it
    finds none, composes the empty string, and without this guard writes a 0-byte file and
    exits 0 — a result any downstream integrity check reads as valid.

    The check is on document count rather than output length. Both reject the same inputs,
    since every document emits at least a heading line, but the count identifies the cause
    and lets the error name it: the wrong layout, and the tool that reads both.

    There is deliberately no lower bound on document count. A floor would catch partial
    truncation but is stale whenever the Atlas shrinks and wrong for small inputs such as
    test fixtures. Truncation is `atlas_source.detect_layout`'s concern; it refuses a
    checkout matching neither layout rather than treating it as a pre-cutover ref.
    """
    if doc_count > 0 and composed.strip():
        return
    raise EmptyCompositionError(
        f"composed 0 documents from {source!r} — refusing to write or hash an empty "
        f"Atlas.\n"
        f"The most likely cause is that {source!r} is in the CONSOLIDATED layout (a few "
        f"`A.<n> - <name>.md` files) while this tool walks the ATOMIZED tree looking for "
        f"`document.md`. Use `sync/atlas_source.py`, which composes from either layout.\n"
        f"Otherwise the checkout is empty or truncated."
    )


def compose_guarded(content_root: str) -> str:
    """`compose`, but refuses to return an empty Atlas. Use this at write/publish points."""
    segments = compose_segments(content_root)
    composed = "\n".join(line for _doc, lines in segments for line in lines)
    guard_composition(composed, len(segments), content_root)
    return composed


# ---------------------------------------------------------------------------
# Roundtrip check
# ---------------------------------------------------------------------------

def diff_summary(actual: str, expected: str, max_lines: int = 40) -> str:
    """Produce a short unified-diff summary for debugging roundtrip mismatches."""
    a_lines = actual.splitlines(keepends=True)
    b_lines = expected.splitlines(keepends=True)
    diff = list(difflib.unified_diff(b_lines, a_lines, fromfile="expected", tofile="actual", n=2))
    if not diff:
        return "(no diff — strings are equal)"
    if len(diff) > max_lines:
        diff = diff[:max_lines] + [f"... ({len(diff) - max_lines} more lines)\n"]
    return "".join(diff)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compose folder-per-document tree into Sky Atlas markdown."
    )
    parser.add_argument("--input", required=True, help="content/ directory to compose from")
    parser.add_argument("--output", help="Output file path (omit when using --check)")
    parser.add_argument("--check", help="Check roundtrip against this file path; exit 1 on diff")
    args = parser.parse_args()

    if not args.output and not args.check:
        parser.error("must pass --output or --check")

    # Guard both paths. An empty composition compared against an empty expected file
    # prints "ROUNDTRIP OK" and exits 0, so --check needs the same guard as --output.
    try:
        composed = compose_guarded(args.input)
    except EmptyCompositionError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if args.check:
        with open(args.check, "r", encoding="utf-8") as f:
            expected = f.read()
        if composed == expected:
            print(f"ROUNDTRIP OK — composed output is byte-identical to {args.check}")
            return 0
        else:
            print(f"ROUNDTRIP MISMATCH — composed output differs from {args.check}")
            print(f"  composed length: {len(composed)} bytes")
            print(f"  expected length: {len(expected)} bytes")
            print()
            print(diff_summary(composed, expected))
            return 1

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(composed)
        print(f"Wrote {len(composed)} bytes to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
