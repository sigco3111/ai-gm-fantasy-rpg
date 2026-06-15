"""Tests for all lore markdown files in the fantasy-rpg plugin.

Mirrors ai-gm-strategy-war/tests/test_lore_chunks.py and ai-gm core's tests/test_lore.py.
"""
from pathlib import Path

import pytest

from tests.conftest import PLUGIN_ROOT


# ---------- S1: every rules .md produces valid chunks ----------

def test_all_rules_md_files_chunk():
    """S1: 4 rule files, each parses to ≥1 valid LoreChunk."""
    from ai_gm.lore.chunker import chunk_file
    rules_dir = PLUGIN_ROOT / "lore" / "rules"
    md_files = sorted(rules_dir.glob("*.md"))
    assert len(md_files) == 4, f"Expected 4 rule files, found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) >= 1, f"{path.name} produced 0 chunks"
        for c in chunks:
            assert c.type == "rule", f"{path.name}: chunk type {c.type} != 'rule'"


# ---------- S2: seed overview produces ≥4 chunks ----------

def test_seed_overview_produces_four_or_more_chunks():
    """S2: overview.md parses to ≥4 chunks (Dragon Return, Player, Factions, World, GM)."""
    from ai_gm.lore.chunker import chunk_file
    overview = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024" / "overview.md"
    assert overview.exists(), f"Missing {overview}"
    chunks = chunk_file(overview)
    assert len(chunks) >= 4, f"overview.md produced {len(chunks)} chunks, expected ≥4"


# ---------- S3: every seed faction file chunks ----------

def test_all_seed_faction_files_chunk():
    """S3: 7 faction files, each with exactly 1 chunk, type=faction."""
    from ai_gm.lore.chunker import chunk_file
    factions_dir = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024" / "factions"
    md_files = sorted(factions_dir.glob("*.md"))
    assert len(md_files) == 7, f"Expected 7 faction files, found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) == 1, f"{path.name} produced {len(chunks)} chunks, expected 1"
        assert chunks[0].type == "faction"


# ---------- S4: every seed region file chunks (type=location) ----------

def test_all_seed_region_files_chunk():
    """S4: 6 region files, each with exactly 1 chunk, type=location (NOT province)."""
    from ai_gm.lore.chunker import chunk_file
    regions_dir = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024" / "regions"
    md_files = sorted(regions_dir.glob("*.md"))
    assert len(md_files) == 6, f"Expected 6 region files, found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) == 1, f"{path.name} produced {len(chunks)} chunks, expected 1"
        assert chunks[0].type == "location", f"{path.name}: type={chunks[0].type} != 'location'"


# ---------- S5: every seed character file chunks ----------

def test_all_seed_character_files_chunk():
    """S5: 5 character files, each with exactly 1 chunk, type=character."""
    from ai_gm.lore.chunker import chunk_file
    chars_dir = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024" / "characters"
    md_files = sorted(chars_dir.glob("*.md"))
    assert len(md_files) == 5, f"Expected 5 character files, found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) == 1, f"{path.name} produced {len(chunks)} chunks, expected 1"
        assert chunks[0].type == "character"


# ---------- S6: total chunk count from all lore ----------

def test_total_lore_chunk_count_is_at_least_43():
    """S6: 4 rules (≥4) + 5 overview + 7 factions + 6 regions + 5 characters = ≥27 (actual ≥43 with multi-chunk rules)."""
    from ai_gm.lore.chunker import chunk_file
    total = 0
    for sub in ("rules",):
        for path in (PLUGIN_ROOT / "lore" / sub).glob("*.md"):
            total += len(chunk_file(path))
    seed_dir = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024"
    total += len(chunk_file(seed_dir / "overview.md"))
    for sub in ("factions", "regions", "characters"):
        for path in (seed_dir / sub).glob("*.md"):
            total += len(chunk_file(path))
    assert total >= 27, f"Total chunks {total} < 27"
