"""Tests for the age-of-dragons-1024 seed against the ai-gm state schema.

Mirrors ai-gm-strategy-war/tests/test_seed_validates.py and ai-gm core's tests/test_state_schema.py.
"""
import json
import re

import pytest


# ---------- S1: seed.json validates against state schema ----------

def test_seed_json_validates_against_state_schema(seed_payload):
    """S1: seed.json (with _meta stripped) passes validate_and_parse('state', ...)."""
    from ai_gm.state.validation import validate_and_parse
    state = validate_and_parse("state", seed_payload)
    assert state.game_id == "age-of-dragons-1024"
    assert state.schema_version == 1
    assert state.turn == 0
    assert len(state.entities) == 18  # 7 factions + 5 characters + 6 provinces


def test_seed_template_json_validates(template_payload):
    """Template (with _about/_meta/_notes stripped) validates too — with minimal entity example."""
    from ai_gm.state.validation import validate_and_parse
    payload = dict(template_payload)
    payload["game_id"] = "demo-template"
    payload["created_at"] = "2026-06-15T00:00:00Z"
    payload["entities"] = [
        {
            "id": "faction_demo",
            "type": "faction",
            "name": "Demo Faction",
            "attributes": {"government": "monarchy"},
        }
    ]
    state = validate_and_parse("state", payload)
    assert state.game_id == "demo-template"


# ---------- S2: all entity ids match the strict pattern ----------

def test_seed_entity_ids_match_strict_pattern(seed_payload):
    """S2: every id matches ^[a-z0-9_-]+$ (lowercase, digits, hyphen, underscore)."""
    pattern = re.compile(r"^[a-z0-9_-]+$")
    for entity in seed_payload["entities"]:
        eid = entity["id"]
        assert pattern.match(eid), f"id '{eid}' violates the strict id pattern"


# ---------- S3: entity type breakdown ----------

def test_seed_entity_type_breakdown(seed_payload):
    """S3: 7 factions, 5 characters, 6 provinces — exact counts."""
    counts = {}
    for entity in seed_payload["entities"]:
        t = entity["type"]
        counts[t] = counts.get(t, 0) + 1
    assert counts == {"faction": 7, "character": 5, "province": 6}, f"Got {counts}"


# ---------- S4: all cross-references resolve ----------

def test_seed_cross_references_resolve(seed_payload):
    """S4: every ruler_id, location_id, controller_id points to an existing entity."""
    ids = {e["id"] for e in seed_payload["entities"]}
    errors = []
    for entity in seed_payload["entities"]:
        attrs = entity.get("attributes", {})
        for ref_key in ("ruler_id", "location_id", "controller_id"):
            ref = attrs.get(ref_key)
            if ref is not None and ref not in ids:
                errors.append(f"{entity['id']}.{ref_key}={ref} (not found)")
    assert not errors, "Dangling references:\n  " + "\n  ".join(errors)


# ---------- S5: faction.stats and faction.resources within bounds ----------

def test_seed_faction_stats_and_resources_in_range(seed_payload):
    """S5: faction.stats.* in [0, 100], faction.resources.* non-negative integer."""
    for entity in seed_payload["entities"]:
        if entity["type"] != "faction":
            continue
        attrs = entity["attributes"]
        for stat, val in attrs.get("stats", {}).items():
            assert 0 <= val <= 100, f"{entity['id']}.stats.{stat}={val} out of [0,100]"
        for res, val in attrs.get("resources", {}).items():
            assert isinstance(val, int) and val >= 0, f"{entity['id']}.resources.{res}={val} not non-neg int"
        for other, val in attrs.get("diplomatic_relations", {}).items():
            assert -100 <= val <= 100, f"{entity['id']}.diplomatic_relations.{other}={val} out of [-100,100]"
            assert other in ids_for_factions(seed_payload), f"{entity['id']}.diplomatic_relations.{other} -> unknown faction"


def ids_for_factions(seed_payload):
    return {e["id"] for e in seed_payload["entities"] if e["type"] == "faction"}
