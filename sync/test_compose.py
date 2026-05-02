#!/usr/bin/env python3
"""Tests for the Atlas compose script (and the decompose↔compose roundtrip)."""

import os
import tempfile

import pytest

from compose import (
    ParsedDoc,
    _child_sort_key,
    _parse_targets_value,
    _unquote_yaml_name,
    build_heading_line,
    compose,
    parse_document_md,
)
from decompose import decompose


# ---------------------------------------------------------------------------
# Fixture sources used for roundtrip tests
# ---------------------------------------------------------------------------

ROUNDTRIP_FIXTURES = [
    # Smallest possible: one Scope, one Article, one Section, one Core.
    """\
# A.0 - Atlas Preamble [Scope]  <!-- UUID: 8650a584-01f8-45d6-882b-c14eab9879c4 -->

This Preamble will be further populated.

## A.0.1 - Atlas Preamble [Article]  <!-- UUID: 56b15d7d-cdd4-4594-bd95-4f094564ac04 -->

This Article contains definitions.

### A.0.1.1 - Definitions [Section]  <!-- UUID: c7d62f28-1d64-4632-8cd8-4f2b44c51bba -->

This Section contains essential definitions.

#### A.0.1.1.1 - Organizational Alignment [Core]  <!-- UUID: 4f6fda1e-7450-4065-8095-e93cb10b3a2a -->

Organizational alignment is a traditional business concept.
""",
    # NR with target attachment + structured-field body.
    """\
# A.0 - Atlas Preamble [Scope]  <!-- UUID: 8650a584-01f8-45d6-882b-c14eab9879c4 -->

This Preamble.

## A.0.1 - Atlas Preamble [Article]  <!-- UUID: 56b15d7d-cdd4-4594-bd95-4f094564ac04 -->

Article body.

### A.0.1.1 - Definitions [Section]  <!-- UUID: c7d62f28-1d64-4632-8cd8-4f2b44c51bba -->

Section body.

#### NR-1 - Research Topic [Needed Research]  <!-- UUID: 2da58ba2-a172-43bd-b7e7-d3d8e69233bf -->

**Content**:

This is research track content that includes the **Content**: structured field.

It spans multiple paragraphs.

#### A.0.1.1.1 - Organizational Alignment [Core]  <!-- UUID: 4f6fda1e-7450-4065-8095-e93cb10b3a2a -->

Core body.
""",
    # Extension segments (.0.3.X annotations and .0.4.X tenets) attached to a
    # specific sub-Core, with a sibling Core after — matches the actual Atlas
    # convention (extensions belong to the most recent regular doc, not split
    # across multiple regular siblings). Empirically: every parent in the
    # current Atlas with extension subtree has at most one regular child at
    # the doc-no level the extension attaches to.
    """\
# A.0 - Atlas Preamble [Scope]  <!-- UUID: 11111111-1111-1111-1111-111111111111 -->

Scope.

## A.0.1 - Article [Article]  <!-- UUID: 22222222-2222-2222-2222-222222222222 -->

Article.

### A.0.1.1 - Section [Section]  <!-- UUID: 33333333-3333-3333-3333-333333333333 -->

Section.

#### A.0.1.1.1 - First Core [Core]  <!-- UUID: 44444444-4444-4444-4444-444444444444 -->

First core.

##### A.0.1.1.1.0.3.1 - Annotation Of First Core [Annotation]  <!-- UUID: 55555555-5555-5555-5555-555555555555 -->

Annotation body.

##### A.0.1.1.1.0.4.1 - Action Tenet Of First Core [Action Tenet]  <!-- UUID: 66666666-6666-6666-6666-666666666666 -->

Action tenet body.

#### A.0.1.1.2 - Second Core [Core]  <!-- UUID: 77777777-7777-7777-7777-777777777777 -->

Second core.
""",
    # Multiple NRs attached to the same target, in numeric order — verifies
    # the "sort by NR number" rule for shared-target NRs.
    """\
# A.0 - Scope [Scope]  <!-- UUID: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa -->

S.

## A.0.1 - Article [Article]  <!-- UUID: bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb -->

A.

### A.0.1.1 - Section [Section]  <!-- UUID: cccccccc-cccc-cccc-cccc-cccccccccccc -->

S body.

#### NR-2 - Second NR [Needed Research]  <!-- UUID: dddddddd-dddd-dddd-dddd-dddddddddddd -->

**Content**:

NR-2 body.

#### NR-3 - Third NR [Needed Research]  <!-- UUID: eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee -->

**Content**:

NR-3 body.

#### A.0.1.1.1 - Core [Core]  <!-- UUID: ffffffff-ffff-ffff-ffff-ffffffffffff -->

Core body.
""",
    # Scenario with Variation — exercises var1 path naming and h6 cap.
    """\
# A.0 - Scope [Scope]  <!-- UUID: 00000000-0000-0000-0000-000000000001 -->

S.

## A.0.1 - Article [Article]  <!-- UUID: 00000000-0000-0000-0000-000000000002 -->

A.

### A.0.1.1 - Section [Section]  <!-- UUID: 00000000-0000-0000-0000-000000000003 -->

S body.

#### A.0.1.1.0.4.1 - Action Tenet [Action Tenet]  <!-- UUID: 00000000-0000-0000-0000-000000000004 -->

Tenet body.

##### A.0.1.1.0.4.1.1.1 - Scenario [Scenario]  <!-- UUID: 00000000-0000-0000-0000-000000000005 -->

**Description**:

Scenario description.

**Finding**:

Misaligned

###### A.0.1.1.0.4.1.1.1.var1 - Scenario Variation [Scenario Variation]  <!-- UUID: 00000000-0000-0000-0000-000000000006 -->

**Description**:

Variation description.
""",
]


def _roundtrip(source_text: str) -> tuple[str, str]:
    """Decompose then compose; return (composed, expected) for assertion."""
    with tempfile.TemporaryDirectory() as tmpdir:
        atlas_path = os.path.join(tmpdir, "Sky Atlas.md")
        with open(atlas_path, "w", encoding="utf-8") as f:
            f.write(source_text)
        content_path = os.path.join(tmpdir, "content")
        decompose(atlas_path, content_path, dry_run=False)
        composed = compose(content_path)
    return composed, source_text


# ---------------------------------------------------------------------------
# Roundtrip integration tests
# ---------------------------------------------------------------------------

class TestRoundtrip:
    @pytest.mark.parametrize("source", ROUNDTRIP_FIXTURES)
    def test_roundtrip_byte_identical(self, source):
        composed, expected = _roundtrip(source)
        assert composed == expected, (
            f"Roundtrip mismatch.\n"
            f"  expected length: {len(expected)}\n"
            f"  composed length: {len(composed)}\n"
            f"  first diff at: {next((i for i, (a, b) in enumerate(zip(composed, expected)) if a != b), 'EOF')}"
        )


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

class TestParseDocumentMd:
    def test_basic_frontmatter(self):
        text = (
            "---\n"
            "id: abc-123\n"
            "docNo: A.0\n"
            "name: Atlas Preamble\n"
            "type: Scope\n"
            "depth: 1\n"
            "childType: sections_and_primary_docs\n"
            "---\n"
            "\n"
            "## A.0 - Atlas Preamble [Scope]\n"
            "\n"
            "Body content.\n"
        )
        doc = parse_document_md(text, ("A", "0"))
        assert doc.uuid == "abc-123"
        assert doc.doc_no == "A.0"
        assert doc.name == "Atlas Preamble"
        assert doc.doc_type == "Scope"
        assert doc.depth == 1
        assert doc.child_type == "sections_and_primary_docs"
        assert doc.targets == []
        # Content lines exclude the heading itself; they include the blank line
        # that follows the heading and the trailing blank.
        assert doc.content_lines == ["", "Body content.", ""]

    def test_nr_targets_parsed(self):
        text = (
            "---\n"
            "id: nr-uuid\n"
            "docNo: NR-1\n"
            "name: Topic\n"
            "type: Needed Research\n"
            "depth: 2\n"
            "childType: needed_research\n"
            "targets: [target-uuid-1]\n"
            "---\n"
            "\n"
            "### NR-1 - Topic [Needed Research]\n"
            "\n"
            "**Content**:\n"
            "\n"
            "Body.\n"
        )
        doc = parse_document_md(text, ("NR", "1"))
        assert doc.targets == ["target-uuid-1"]
        assert "**Content**:" in "\n".join(doc.content_lines)

    def test_quoted_name_unescaped(self):
        text = (
            "---\n"
            "id: u\n"
            "docNo: A.0\n"
            'name: "Defining \\"Severe Actions\\""\n'
            "type: Scope\n"
            "depth: 1\n"
            "childType: sections_and_primary_docs\n"
            "---\n"
            "\n"
            '# A.0 - Defining "Severe Actions" [Scope]\n'
        )
        doc = parse_document_md(text, ("A", "0"))
        assert doc.name == 'Defining "Severe Actions"'


# ---------------------------------------------------------------------------
# Sibling sort
# ---------------------------------------------------------------------------

class TestChildSortKey:
    def test_real_doc_before_phantom(self, tmp_path):
        # Build: parent/1/document.md (real), parent/0/ (phantom — no document.md)
        parent = tmp_path / "parent"
        (parent / "1").mkdir(parents=True)
        (parent / "1" / "document.md").write_text("doc")
        (parent / "0").mkdir()
        # "0" sorts AFTER "1" (real-doc-first rule), even though it's numerically smaller.
        names = sorted(["0", "1"], key=lambda c: _child_sort_key(str(parent), c))
        assert names == ["1", "0"]

    def test_real_docs_numeric_ascending(self, tmp_path):
        parent = tmp_path / "p"
        for n in ("1", "2", "10"):
            (parent / n).mkdir(parents=True)
            (parent / n / "document.md").write_text("d")
        # 10 must sort after 2 (numeric, not lexicographic).
        names = sorted(["10", "2", "1"], key=lambda c: _child_sort_key(str(parent), c))
        assert names == ["1", "2", "10"]


# ---------------------------------------------------------------------------
# Heading line construction
# ---------------------------------------------------------------------------

class TestBuildHeadingLine:
    def test_h1_scope(self):
        d = ParsedDoc(("A", "0"), "u-1", "A.0", "Atlas Preamble", "Scope", 1,
                       "sections_and_primary_docs", [], [])
        assert build_heading_line(d, 1) == "# A.0 - Atlas Preamble [Scope]  <!-- UUID: u-1 -->"

    def test_h6_capped(self):
        d = ParsedDoc(("A", "0"), "u-2", "A.0.1.1.1.1.1", "X", "Core", 6,
                       "sections_and_primary_docs", [], [])
        assert build_heading_line(d, 6).startswith("###### ")


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

class TestUnquoteYamlName:
    def test_unquoted(self):
        assert _unquote_yaml_name("Atlas Preamble") == "Atlas Preamble"

    def test_quoted_with_escaped_quote(self):
        assert _unquote_yaml_name('"Defining \\"Severe Actions\\""') == 'Defining "Severe Actions"'


class TestParseTargetsValue:
    def test_single(self):
        assert _parse_targets_value("[abc]") == ["abc"]

    def test_multi(self):
        assert _parse_targets_value("[abc, def, ghi]") == ["abc", "def", "ghi"]

    def test_empty_list(self):
        assert _parse_targets_value("[]") == []

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            _parse_targets_value("not a list")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
