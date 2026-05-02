#!/usr/bin/env python3
"""Tests for the Atlas decompose script."""

import os
import tempfile

import pytest

from decompose import (
    Document,
    IndexEntry,
    build_document_md,
    build_frontmatter,
    build_heading,
    build_index_md,
    compute_children,
    decompose,
    doc_folder_path,
    parse_atlas,
    plan_output,
    yaml_quote_name,
)


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

SAMPLE_ATLAS = """\
# A.0 - Atlas Preamble [Scope]  <!-- UUID: 8650a584-01f8-45d6-882b-c14eab9879c4 -->

This Preamble will be further populated in later iterations of the Atlas.

## A.0.1 - Atlas Preamble [Article]  <!-- UUID: 56b15d7d-cdd4-4594-bd95-4f094564ac04 -->

This Article contains definitions and general provisions.

### A.0.1.1 - Definitions [Section]  <!-- UUID: c7d62f28-1d64-4632-8cd8-4f2b44c51bba -->

This Section contains essential definitions.

#### A.0.1.1.1 - Organizational Alignment [Core]  <!-- UUID: 4f6fda1e-7450-4065-8095-e93cb10b3a2a -->

Organizational alignment is a traditional business concept.

#### NR-1 - Systematic Basis Of Adjudication, Fact-Finding And Evidence [Needed Research]  <!-- UUID: 2da58ba2-a172-43bd-b7e7-d3d8e69233bf -->

**Content**:

This need is an extensive Research Track.

#### A.0.1.1.2 - Ecosystem Intelligence [Core]  <!-- UUID: 5e2e1397-ff87-43ce-a742-e5a68dc89a44 -->

"Ecosystem Intelligence" characterizes a decentralized ecosystem.
"""

SAMPLE_WITH_VAR = """\
##### A.1.4.5.0.4.1.1.1 - Alternating Between Two Roles [Scenario]  <!-- UUID: d5e82bc9-9d46-4d1b-a580-dc695d4a3c19 -->

**Description**:

Entity occupied the role of a ranked AD.

**Finding**:

Misaligned

**Additional Guidance**:

The Facilitator should derecognize Entity.

###### A.1.4.5.0.4.1.1.1.var1 - Alternating - var. 1 [Scenario Variation]  <!-- UUID: b7eb5043-6f80-4dcf-8392-fbb3e200cf9e -->

**Description**:

Entity occupied the role of an unranked AD.

**Finding**:

Aligned

**Additional Guidance**:

No action needed.
"""

SAMPLE_TYPE_SPEC = """\
##### A.1.2.2.2.1 - The Type Specification Type [Type Specification]  <!-- UUID: 468d192b-83bc-45ab-896f-53e8ca307135 -->

[See below]

**Components**:

"Type Name": The name of the Document Type

**Doc Identifier Rules**:

Must follow Primary Document rules.

**Additional Logic**:

Rules must be followed.

**Type Category**:

Primary Document

**Type Name**:

Type Specification

**Type Overview**:

Used for Type Specification Documents.
"""


# ---------------------------------------------------------------------------
# Test parsing
# ---------------------------------------------------------------------------

class TestParsing:
    def test_parse_basic(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        assert len(docs) == 6

    def test_parse_scope(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        scope = docs[0]
        assert scope.doc_no == "A.0"
        assert scope.name == "Atlas Preamble"
        assert scope.doc_type == "Scope"
        assert scope.uuid == "8650a584-01f8-45d6-882b-c14eab9879c4"
        assert scope.heading_level == 1

    def test_parse_article(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        article = docs[1]
        assert article.doc_no == "A.0.1"
        assert article.doc_type == "Article"
        assert article.heading_level == 2

    def test_parse_nr(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        nr = docs[4]
        assert nr.doc_no == "NR-1"
        assert nr.doc_type == "Needed Research"
        assert nr.is_nr

    def test_content_extracted(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        scope = docs[0]
        assert "This Preamble will be further populated" in scope.content

    def test_nr_content_preserved(self):
        # Content is no longer stripped — NRs retain their **Content**: field
        # and body text verbatim so compose can roundtrip.
        docs = parse_atlas(SAMPLE_ATLAS)
        nr = docs[4]
        assert "**Content**:" in nr.content
        assert "Research Track" in nr.content

    def test_nr_target_captured(self):
        # NR-1 in SAMPLE_ATLAS sits directly after A.0.1.1.1 (Core).
        # Its placement-target should be that doc's UUID.
        docs = parse_atlas(SAMPLE_ATLAS)
        nr = docs[4]
        assert nr.targets == ["4f6fda1e-7450-4065-8095-e93cb10b3a2a"]

    def test_content_between_headings(self):
        docs = parse_atlas(SAMPLE_ATLAS)
        core = docs[3]  # A.0.1.1.1
        assert "traditional business concept" in core.content
        # Should not contain next doc's content
        assert "Ecosystem Intelligence" not in core.content

    def test_parse_scenario_var(self):
        docs = parse_atlas(SAMPLE_WITH_VAR)
        assert len(docs) == 2
        scenario = docs[0]
        var = docs[1]
        assert scenario.doc_type == "Scenario"
        assert var.doc_type == "Scenario Variation"
        assert var.doc_no == "A.1.4.5.0.4.1.1.1.var1"

    def test_scenario_content_preserved(self):
        # **Description**: / **Finding**: / **Additional Guidance**: are
        # preserved verbatim now (no extra-field stripping).
        docs = parse_atlas(SAMPLE_WITH_VAR)
        scenario = docs[0]
        assert "**Description**:" in scenario.content
        assert "Entity occupied" in scenario.content

    def test_type_spec_content_preserved(self):
        # All structured-field content is preserved for byte-faithful roundtrip.
        docs = parse_atlas(SAMPLE_TYPE_SPEC)
        assert len(docs) == 1
        ts = docs[0]
        assert "[See below]" in ts.content
        assert "**Components**:" in ts.content
        assert '"Type Name": The name of the Document Type' in ts.content


# ---------------------------------------------------------------------------
# Test depth calculation
# ---------------------------------------------------------------------------

class TestDepth:
    def test_scope_depth(self):
        doc = Document("A.0", "Test", "Scope", "uuid", 1)
        assert doc.depth == 1

    def test_article_depth(self):
        doc = Document("A.0.1", "Test", "Article", "uuid", 2)
        assert doc.depth == 3

    def test_section_depth(self):
        doc = Document("A.0.1.1", "Test", "Section", "uuid", 3)
        assert doc.depth == 4

    def test_core_depth(self):
        doc = Document("A.0.1.1.1", "Test", "Core", "uuid", 4)
        assert doc.depth == 5

    def test_deep_core_depth(self):
        doc = Document("A.0.1.2.1.1", "Test", "Core", "uuid", 5)
        assert doc.depth == 6

    def test_annotation_depth(self):
        doc = Document("A.0.1.2.1.1.0.3.1", "Test", "Annotation", "uuid", 6)
        assert doc.depth == 9

    def test_tenet_depth(self):
        doc = Document("A.0.1.2.1.1.0.4.1", "Test", "Action Tenet", "uuid", 6)
        assert doc.depth == 9

    def test_scenario_depth(self):
        doc = Document("A.1.4.5.0.4.1.1.1", "Test", "Scenario", "uuid", 5)
        assert doc.depth == 9

    def test_var_depth(self):
        doc = Document("A.1.4.5.0.4.1.1.1.var1", "Test", "Scenario Variation", "uuid", 6)
        assert doc.depth == 9  # segments - 1 for var

    def test_nr_depth(self):
        doc = Document("NR-1", "Test", "Needed Research", "uuid", 4)
        assert doc.depth == 2

    def test_nr_depth_always_2(self):
        doc = Document("NR-18", "Test", "Needed Research", "uuid", 5)
        assert doc.depth == 2


# ---------------------------------------------------------------------------
# Test output heading level
# ---------------------------------------------------------------------------

class TestOutputHeadingLevel:
    def test_scope_heading(self):
        doc = Document("A.0", "Test", "Scope", "uuid", 1)
        assert doc.output_heading_level == 2  # depth 1 + 1

    def test_article_heading(self):
        doc = Document("A.0.1", "Test", "Article", "uuid", 2)
        assert doc.output_heading_level == 4  # depth 3 + 1

    def test_section_heading(self):
        doc = Document("A.0.1.1", "Test", "Section", "uuid", 3)
        assert doc.output_heading_level == 5  # depth 4 + 1

    def test_core_heading(self):
        doc = Document("A.0.1.1.1", "Test", "Core", "uuid", 4)
        assert doc.output_heading_level == 6  # depth 5 + 1, capped at 6

    def test_deep_heading_capped(self):
        doc = Document("A.0.1.2.1.1", "Test", "Core", "uuid", 5)
        assert doc.output_heading_level == 6  # depth 6 + 1 > 6, capped

    def test_nr_heading(self):
        doc = Document("NR-1", "Test", "Needed Research", "uuid", 4)
        assert doc.output_heading_level == 3  # depth 2 + 1


# ---------------------------------------------------------------------------
# Test child type
# ---------------------------------------------------------------------------

class TestChildType:
    def test_scope(self):
        doc = Document("A.0", "T", "Scope", "u", 1)
        assert doc.child_type == "sections_and_primary_docs"

    def test_article(self):
        doc = Document("A.0.1", "T", "Article", "u", 2)
        assert doc.child_type == "articles"

    def test_section(self):
        doc = Document("A.0.1.1", "T", "Section", "u", 3)
        assert doc.child_type == "sections_and_primary_docs"

    def test_active_data(self):
        doc = Document("A.1.0.6.1", "T", "Active Data", "u", 6)
        assert doc.child_type == "active_data"

    def test_annotation(self):
        doc = Document("A.1.0.3.1", "T", "Annotation", "u", 5)
        assert doc.child_type == "annotations"

    def test_scenario(self):
        doc = Document("A.1.1.1", "T", "Scenario", "u", 5)
        assert doc.child_type == "tenets"

    def test_scenario_variation(self):
        doc = Document("A.1.1.var1", "T", "Scenario Variation", "u", 6)
        assert doc.child_type == "tenets"

    def test_needed_research(self):
        doc = Document("NR-1", "T", "Needed Research", "u", 4)
        assert doc.child_type == "needed_research"


# ---------------------------------------------------------------------------
# Test folder path
# ---------------------------------------------------------------------------

class TestFolderPath:
    def test_scope_path(self):
        doc = Document("A.0", "T", "Scope", "u", 1)
        assert doc.folder_path_segments == ["A", "0"]

    def test_deep_path(self):
        doc = Document("A.6.1.1.1.2", "T", "Core", "u", 6)
        assert doc.folder_path_segments == ["A", "6", "1", "1", "1", "2"]

    def test_var_path(self):
        doc = Document("A.1.4.5.0.4.1.1.1.var1", "T", "Scenario Variation", "u", 6)
        assert doc.folder_path_segments == ["A", "1", "4", "5", "0", "4", "1", "1", "1", "var1"]

    def test_nr_path(self):
        doc = Document("NR-7", "T", "Needed Research", "u", 4)
        assert doc.folder_path_segments == ["NR", "7"]


# ---------------------------------------------------------------------------
# Test YAML quoting
# ---------------------------------------------------------------------------

class TestYamlQuoting:
    def test_simple_name(self):
        assert yaml_quote_name("Atlas Preamble") == "Atlas Preamble"

    def test_name_with_comma(self):
        assert yaml_quote_name("Adjudication, Fact-Finding And Evidence") == "Adjudication, Fact-Finding And Evidence"

    def test_name_with_parentheses(self):
        assert yaml_quote_name("Scope Artifact (SA)") == "Scope Artifact (SA)"

    def test_name_with_double_quotes(self):
        result = yaml_quote_name('Defining "Severe Actions"')
        assert result == '"Defining \\"Severe Actions\\""'

    def test_name_with_colon(self):
        result = yaml_quote_name("Step 4: Smart Burn")
        assert result.startswith('"') and result.endswith('"')

    def test_name_with_ampersand(self):
        result = yaml_quote_name("Security & Embedding")
        assert result.startswith('"') and result.endswith('"')

    def test_name_with_apostrophe(self):
        result = yaml_quote_name("One Month's Budget")
        assert result.startswith('"') and result.endswith('"')


# ---------------------------------------------------------------------------
# Test frontmatter
# ---------------------------------------------------------------------------

class TestFrontmatter:
    def test_basic_frontmatter(self):
        doc = Document("A.0", "Atlas Preamble", "Scope", "8650a584-01f8-45d6-882b-c14eab9879c4", 1)
        fm = build_frontmatter(doc)
        assert "id: 8650a584-01f8-45d6-882b-c14eab9879c4" in fm
        assert "docNo: A.0" in fm
        assert "name: Atlas Preamble" in fm
        assert "type: Scope" in fm
        assert "depth: 1" in fm
        assert "childType: sections_and_primary_docs" in fm
        # Non-NR docs should not have a targets field.
        assert "targets:" not in fm

    def test_nr_frontmatter_includes_targets(self):
        # NRs should emit `targets: [<UUID>]` in frontmatter.
        nr = Document("NR-1", "Topic", "Needed Research",
                      "2da58ba2-a172-43bd-b7e7-d3d8e69233bf", 4)
        nr.targets = ["8650a584-01f8-45d6-882b-c14eab9879c4"]
        fm = build_frontmatter(nr)
        assert "targets: [8650a584-01f8-45d6-882b-c14eab9879c4]" in fm

    def test_nr_with_no_targets_omits_field(self):
        # An NR without an attached target (orphan) shouldn't emit an empty list.
        nr = Document("NR-99", "Orphan", "Needed Research", "uuid", 4)
        fm = build_frontmatter(nr)
        assert "targets:" not in fm


# ---------------------------------------------------------------------------
# Test heading generation
# ---------------------------------------------------------------------------

class TestHeading:
    def test_scope_heading(self):
        doc = Document("A.0", "Atlas Preamble", "Scope", "u", 1)
        assert build_heading(doc) == "## A.0 - Atlas Preamble [Scope]"

    def test_nr_heading(self):
        doc = Document("NR-1", "Research Topic", "Needed Research", "u", 4)
        assert build_heading(doc) == "### NR-1 - Research Topic [Needed Research]"


# ---------------------------------------------------------------------------
# Test index generation
# ---------------------------------------------------------------------------

class TestIndex:
    def test_basic_index(self):
        entries = [
            IndexEntry("A.0.1.1.1", "Organizational Alignment", "1"),
            IndexEntry("A.0.1.1.2", "Ecosystem Intelligence", "2"),
        ]
        result = build_index_md("content/A/0/1/1", entries)
        assert "childCount: 2" in result
        assert "path: content/A/0/1/1" in result
        assert "- [A.0.1.1.1 - Organizational Alignment](1/document.md)" in result
        assert "- [A.0.1.1.2 - Ecosystem Intelligence](2/document.md)" in result


# ---------------------------------------------------------------------------
# Test children computation
# ---------------------------------------------------------------------------

class TestComputeChildren:
    def test_basic_children(self):
        docs = [
            Document("A.0", "P", "Scope", "u1", 1),
            Document("A.0.1", "C1", "Article", "u2", 2),
            Document("A.0.1.1", "C2", "Section", "u3", 3),
        ]
        children = compute_children(docs)
        assert "A" in children
        assert len(children["A"]) == 1  # A.0
        assert "A/0" in children
        assert len(children["A/0"]) == 1  # A.0.1
        assert "A/0/1" in children
        assert len(children["A/0/1"]) == 1  # A.0.1.1


# ---------------------------------------------------------------------------
# Test full document generation
# ---------------------------------------------------------------------------

class TestDocumentMd:
    def test_with_content(self):
        doc = Document("A.0", "Atlas Preamble", "Scope", "8650a584-01f8-45d6-882b-c14eab9879c4", 1)
        doc.content = "\nThis Preamble will be further populated in later iterations of the Atlas."
        result = build_document_md(doc)
        assert result.startswith("---\n")
        assert "## A.0 - Atlas Preamble [Scope]" in result
        assert "This Preamble will be further populated" in result

    def test_without_content(self):
        doc = Document("NR-1", "Topic", "Needed Research", "uuid", 4)
        doc.content = ""
        result = build_document_md(doc)
        assert result.endswith("### NR-1 - Topic [Needed Research]\n")


# ---------------------------------------------------------------------------
# Integration test
# ---------------------------------------------------------------------------

class TestIntegration:
    def test_full_decompose(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Write sample atlas to temp file
            atlas_path = os.path.join(tmpdir, "atlas.md")
            with open(atlas_path, "w") as f:
                f.write(SAMPLE_ATLAS)

            output_path = os.path.join(tmpdir, "content")
            files = decompose(atlas_path, output_path, dry_run=False)

            # Check that files were created
            assert os.path.isfile(os.path.join(output_path, "A", "0", "document.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "0", "1", "document.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "0", "1", "1", "document.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "0", "1", "1", "1", "document.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "0", "1", "1", "2", "document.md"))
            assert os.path.isfile(os.path.join(output_path, "NR", "1", "document.md"))

            # Check index files
            assert os.path.isfile(os.path.join(output_path, "_index.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "_index.md"))
            assert os.path.isfile(os.path.join(output_path, "NR", "_index.md"))
            assert os.path.isfile(os.path.join(output_path, "A", "0", "_index.md"))

            # Check scope document content
            with open(os.path.join(output_path, "A", "0", "document.md")) as f:
                content = f.read()
            assert "id: 8650a584-01f8-45d6-882b-c14eab9879c4" in content
            assert "depth: 1" in content
            assert "## A.0 - Atlas Preamble [Scope]" in content

            # Check NR document
            with open(os.path.join(output_path, "NR", "1", "document.md")) as f:
                content = f.read()
            assert "depth: 2" in content
            assert "### NR-1" in content
            # NRs preserve their structured-field content verbatim now —
            # `**Content**:` is the source format and decompose keeps it.
            assert "**Content**:" in content
            assert "Research Track" in content
            # NR target should be captured (NR-1 in SAMPLE follows A.0.1.1.1).
            assert "targets: [4f6fda1e-7450-4065-8095-e93cb10b3a2a]" in content

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            atlas_path = os.path.join(tmpdir, "atlas.md")
            with open(atlas_path, "w") as f:
                f.write(SAMPLE_ATLAS)

            output_path = os.path.join(tmpdir, "content")
            files = decompose(atlas_path, output_path, dry_run=True)

            assert len(files) > 0
            assert not os.path.exists(output_path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
