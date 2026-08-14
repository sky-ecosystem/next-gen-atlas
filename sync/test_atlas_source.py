"""Tests for `atlas_source`, the single entry point every consumer calls.

Coverage here starts with the module importing at all. `atlas_source` is imported by
consumers rather than by the rest of the suite, so a stale import inside it — a name
removed from `partition`, for instance — breaks every consumer while the rest of the
tests stay green.
"""
from __future__ import annotations

import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from atlas_source import (ATOMIZED, CONSOLIDATED, LayoutError,  # noqa: E402
                          detect_layout, load_composed)
from compose import compose                                      # noqa: E402
from decompose import decompose                                  # noqa: E402
from partition import write_split                                # noqa: E402

_CONTENT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

pytestmark = pytest.mark.skipif(
    not os.path.isdir(_CONTENT), reason="no content/ directory")


def _both_layouts(tmp: str) -> tuple[str, str]:
    """Return (atomized_dir, consolidated_dir) holding the same Atlas."""
    layout = detect_layout(_CONTENT)
    if layout == ATOMIZED:
        atom = _CONTENT
        cons = os.path.join(tmp, "cons")
        write_split(atom, cons)
    else:
        cons = _CONTENT
        md = os.path.join(tmp, "c.md")
        with open(md, "w", encoding="utf-8") as f:
            f.write(load_composed(cons))
        atom = os.path.join(tmp, "atom", "content")
        decompose(md, atom, write_indexes=False)
    return atom, cons


def test_the_module_imports_at_all():
    """A stale import inside the module leaves every consumer broken."""
    import atlas_source
    assert callable(atlas_source.load_composed)


def test_detects_each_layout():
    with tempfile.TemporaryDirectory() as tmp:
        atom, cons = _both_layouts(tmp)
        assert detect_layout(atom) == ATOMIZED
        assert detect_layout(cons) == CONSOLIDATED


def test_both_layouts_compose_identically():
    """Both layouts compose to the same Atlas, so no consumer needs to know which one a
    checkout is in."""
    with tempfile.TemporaryDirectory() as tmp:
        atom, cons = _both_layouts(tmp)
        assert load_composed(atom) == load_composed(cons)
        assert load_composed(atom) == compose(atom)


def test_empty_directory_raises_rather_than_reading_as_pre_cutover():
    """A walk finding no `document.md` returns `[]`, which downstream reads as a
    pre-cutover ref. That makes a truncated or half-fetched checkout indistinguishable
    from an old one, so a directory matching neither layout must raise rather than be
    classified."""
    with tempfile.TemporaryDirectory() as tmp:
        with pytest.raises(LayoutError, match="neither layout"):
            detect_layout(tmp)


def test_half_migrated_checkout_raises():
    """Both layouts present at once means a migration stopped midway. Guessing either way
    silently produces a wrong Atlas; refusing is the only safe answer."""
    with tempfile.TemporaryDirectory() as tmp:
        _atom, cons = _both_layouts(tmp)
        mixed = os.path.join(tmp, "mixed")
        os.makedirs(os.path.join(mixed, "A", "0"))
        open(os.path.join(mixed, "A", "0", "document.md"), "w").close()
        for f in os.listdir(cons):
            if f.endswith(".md"):
                open(os.path.join(mixed, f), "w").close()
                break
        with pytest.raises(LayoutError, match="half-finished"):
            detect_layout(mixed)


def test_missing_directory_raises():
    with pytest.raises(LayoutError):
        detect_layout("/nonexistent/atlas/content")
