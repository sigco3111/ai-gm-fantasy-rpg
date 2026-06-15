"""End-to-end tests: load the age-of-dragons-1024 seed into ai-gm core and exercise the tool chain.

Mirrors ai-gm-strategy-war/tests/test_e2e_integration.py.
Requires ai-gm to be importable (PYTHONPATH=../ai-gm/src).
"""
import json
from pathlib import Path

import pytest

from tests.conftest import PLUGIN_ROOT


# ---------- S1: start_game from the seed payload ----------

def test_e2e_start_game_from_seed_creates_state_file(tmp_games_dir, seed_payload):
    """S1: calling start_game_logic with the seed payload returns ok:true and persists state.json."""
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic

    store = StateStore(tmp_games_dir)
    result = start_game_logic(payload=seed_payload, store=store)

    assert result["ok"] is True, f"start_game failed: {result.get('error')}"
    assert result["game_id"] == "age-of-dragons-1024"

    state_file = tmp_games_dir / "age-of-dragons-1024" / "state.json"
    assert state_file.exists(), f"state.json not written to {state_file}"
    on_disk = json.loads(state_file.read_text())
    assert on_disk["game_id"] == "age-of-dragons-1024"
    assert len(on_disk["entities"]) == 18


# ---------- S2: first turn advances the state ----------

def test_e2e_advance_first_turn_succeeds(tmp_games_dir, seed_payload):
    """S2: a valid first-turn event (actor=character_lyndwell, action=custom) advances turn 0→1."""
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic
    from ai_gm.tools.advance_turn import advance_turn_logic

    store = StateStore(tmp_games_dir)
    start_result = start_game_logic(payload=seed_payload, store=store)
    assert start_result["ok"] is True

    event = {
        "event_id": "ev-e2e-001",
        "turn": 0,
        "actor_id": "character_lyndwell",
        "action": "custom",
        "payload": {"region": "province_shallowstone", "verb": "explore"},
        "reason": "Player character begins exploration of the ruined town.",
    }
    advance_result = advance_turn_logic(game_id="age-of-dragons-1024", event=event, store=store)
    assert advance_result.get("ok") is True, f"advance_turn failed: {advance_result.get('error')}"
    assert advance_result["turn"] == 1, f"Expected turn 1, got {advance_result.get('turn')}"

    # State file should now show turn 1 with the event appended
    on_disk = json.loads((tmp_games_dir / "age-of-dragons-1024" / "state.json").read_text())
    assert on_disk["turn"] == 1
    assert any(e.get("event_ref") == "ev-e2e-001" for e in on_disk.get("event_log", [])), \
        f"Event not in event_log: {on_disk.get('event_log')}"


# ---------- S3: read_lore returns a verbatim chunk ----------

def test_e2e_read_lore_finds_kargad_chunk(tmp_games_dir):
    """S3: write the dragonclaw_horde.md content to a per-game world.md; read_lore returns it."""
    from ai_gm.lore.chunker import chunk_file
    from ai_gm.tools.read_lore import read_lore_logic

    game_id = "kargad-chunk-test"
    game_dir = tmp_games_dir / game_id
    game_dir.mkdir(parents=True, exist_ok=True)
    lore_dir = game_dir / "lore"
    lore_dir.mkdir(exist_ok=True)
    kargad_src = PLUGIN_ROOT / "lore" / "seeds" / "age-of-dragons-1024" / "factions" / "faction_dragonclaw_horde.md"
    lore_dir.joinpath("world.md").write_text(kargad_src.read_text(encoding="utf-8"), encoding="utf-8")

    chunks = chunk_file(lore_dir / "world.md")
    assert len(chunks) >= 1
    kargad_chunks = [c for c in chunks if "용발톱" in c.name]
    assert len(kargad_chunks) == 1, f"Expected 1 Dragonclaw Horde chunk, found {len(kargad_chunks)}"
    assert kargad_chunks[0].type == "faction"

    result = read_lore_logic(
        game_id=game_id,
        chunk_name="용발톱 무리 (Dragonclaw Horde)",
        root=tmp_games_dir,
    )
    assert result["ok"] is True, f"read_lore failed: {result.get('error')}"
    assert "Kargad" in result["chunk"]["content"] or "용발톱" in result["chunk"]["content"]


# ---------- S4: read_state_history shows the audit log ----------

def test_e2e_read_state_history_shows_audit(tmp_games_dir, seed_payload):
    """S4: after advance_turn, read_state_history returns the audit entry."""
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic
    from ai_gm.tools.advance_turn import advance_turn_logic
    from ai_gm.tools.read_state_history import read_state_history_logic

    store = StateStore(tmp_games_dir)
    start_result = start_game_logic(payload=seed_payload, store=store)
    assert start_result["ok"] is True

    event = {
        "event_id": "ev-e2e-audit",
        "turn": 0,
        "actor_id": "character_lyndwell",
        "action": "custom",
        "payload": {"note": "audit test"},
        "reason": "Test audit entry.",
    }
    advance_result = advance_turn_logic(game_id="age-of-dragons-1024", event=event, store=store)
    assert advance_result["ok"] is True, f"advance_turn failed: {advance_result.get('error')}"

    history = read_state_history_logic(game_id="age-of-dragons-1024")
    assert history["ok"] is True
    assert history["count"] >= 1, f"history count {history['count']} < 1; entries={history['entries']}"
    assert any(e.get("event_id") == "ev-e2e-audit" for e in history["entries"])
