"""Tests for the chunk delimiter format used by all lore markdown files.

This is the GATE for the fantasy-rpg plugin: every rules file, every seed entity
file, and every overview section MUST use the H2 [CHUNK: TYPE -- NAME] format
that the ai-gm core's chunker expects.

Mirrors ai-gm core's tests/test_lore.py and ai-gm-strategy-war/tests/test_lore_chunks.py.
"""
from pathlib import Path

import pytest

from tests.conftest import PLUGIN_ROOT


# ---------- S1: the regex matches the exact format we use ----------

def test_chunk_header_regex_matches_valid_header():
    """A well-formed H2 [CHUNK: ...] header must match the core's regex."""
    from ai_gm.lore.chunker import _HEADER_RE
    md = "## [CHUNK: rule -- COMBAT]\n\nBody text.\n"
    matches = list(_HEADER_RE.finditer(md))
    assert len(matches) == 1, f"Expected 1 match, got {len(matches)}"
    m = matches[0]
    assert m.group(1) == "rule"
    assert m.group(2).strip() == "COMBAT"


def test_chunk_header_regex_rejects_malformed_header():
    """A header missing the brackets must NOT match."""
    from ai_gm.lore.chunker import _HEADER_RE
    md = "## CHUNK: rule -- COMBAT\n\nBody text.\n"
    matches = list(_HEADER_RE.finditer(md))
    assert len(matches) == 0, f"Expected 0 matches, got {len(matches)}"


def test_chunk_header_regex_tolerates_em_dash_separator():
    """The regex should accept the em-dash variant (—) used in some chunks."""
    from ai_gm.lore.chunker import _HEADER_RE
    md = "## [CHUNK: faction — Shallowstone Defenders]\n\nBody text.\n"
    matches = list(_HEADER_RE.finditer(md))
    assert len(matches) == 1, f"Expected 1 match with em-dash, got {len(matches)}"


# ---------- S2: the fixture file actually parses to a LoreChunk ----------

def test_sample_fixture_chunks_to_one_lorechunk():
    """The sample_chunk.md fixture must produce exactly 1 valid LoreChunk."""
    from ai_gm.lore.chunker import chunk_file
    fixture_path = PLUGIN_ROOT / "tests" / "fixtures" / "sample_chunk.md"
    assert fixture_path.exists(), f"Fixture missing: {fixture_path}"
    chunks = chunk_file(fixture_path)
    assert len(chunks) == 1, f"Expected 1 chunk, got {len(chunks)}"
    c = chunks[0]
    assert c.type == "rule"
    assert c.name == "COMBAT"
    assert "Melee" in c.content
    assert "combat" in c.triggers
    assert c.priority == 7
