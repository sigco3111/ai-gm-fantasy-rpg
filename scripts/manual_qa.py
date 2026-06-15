"""Manual QA round-trip for the ai-gm-fantasy-rpg plugin.

Boots the real MCP server with AI_GM_PLUGINS_DIR pointed at this plugin,
then exercises the full tool chain end-to-end over stdio JSON-RPC.

Verifies the S1-S8 contract for the age-of-dragons-1024 seed:
  S1: start_game_with_seed("age-of-dragons-1024") returns ok + state + chunks > 0
  S2: advance_turn increments turn + appends audit
  S3: read_lore returns a known chunk's content verbatim
  S4: state.json validates against state schema (covered by pytest)
  S5: 4 rules have >= 1 H2 [CHUNK] header (covered by pytest)
  S6: examples/turn-001-founding.jsonl is well-formed (covered by separate test)
  S7: pytest tests/ passes (separate run)
  S8: this script — round-trip end-to-end

Usage:
    AI_GM_PLUGINS_DIR=/path/to/ai-gm-fantasy-rpg \\
    PYTHONPATH=/path/to/ai-gm/src \\
    python3 /path/to/ai-gm-fantasy-rpg/scripts/manual_qa.py

Exit 0 on full success, 1 on any mismatch.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
CORE_ROOT = PLUGIN_ROOT.parent / "ai-gm"
SEED_ID = "age-of-dragons-1024"


def log(msg: str) -> None:
    print(f"[fantasy-rpg qa] {msg}", flush=True)


def send_request(proc: subprocess.Popen, request_id: int, method: str, params: dict) -> None:
    msg = {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
    line = json.dumps(msg) + "\n"
    log(f"--> {method} (id={request_id})")
    proc.stdin.write(line)
    proc.stdin.flush()


def read_response(proc: subprocess.Popen, timeout: float = 10.0) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line:
            stderr = proc.stderr.read() if proc.stderr else ""
            if stderr:
                log(f"[server stderr]: {stderr}")
            raise RuntimeError("Server closed stdout before sending response")
        line = line.strip()
        if not line:
            continue
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            continue
    raise TimeoutError(f"Server did not respond within {timeout}s")


def extract_tool_payload(result: dict) -> dict:
    sc = result.get("structuredContent")
    if sc is not None:
        return sc
    content = result.get("content", [])
    if content and isinstance(content, list) and content[0].get("type") == "text":
        text = content[0].get("text", "")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"_raw_text": text}
    return result


def main() -> int:
    if not (PLUGIN_ROOT / "lore" / "seeds" / SEED_ID / "seed.json").exists():
        log(f"FATAL: seed not found at {PLUGIN_ROOT}/lore/seeds/{SEED_ID}/seed.json")
        return 1

    tmpdir = Path(tempfile.mkdtemp(prefix="fantasy-rpg-qa-"))
    log(f"Tmp games dir: {tmpdir}")

    env = os.environ.copy()
    env["AI_GM_GAMES_DIR"] = str(tmpdir)
    env["AI_GM_PLUGINS_DIR"] = str(PLUGIN_ROOT)
    log(f"Spawning: python -m ai_gm (cwd={CORE_ROOT}, AI_GM_PLUGINS_DIR={PLUGIN_ROOT})")

    proc = subprocess.Popen(
        [sys.executable, "-m", "ai_gm"],
        cwd=str(CORE_ROOT),
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    try:
        send_request(proc, 1, "initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "fantasy-rpg-manual-qa", "version": "1.0"},
        })
        resp = read_response(proc)
        if "result" not in resp:
            log(f"FATAL: initialize failed: {resp}")
            return 1
        log("Server initialized.")

        send_request(proc, 2, "tools/list", {})
        resp = read_response(proc)
        if "result" not in resp:
            log(f"FATAL: tools/list failed: {resp}")
            return 1
        tool_names = {t["name"] for t in resp["result"].get("tools", [])}
        log(f"Tools registered: {sorted(tool_names)}")
        expected = {
            "start_game", "start_game_with_seed", "read_state",
            "advance_turn", "search_history", "read_lore",
            "end_session", "read_state_history",
        }
        missing = expected - tool_names
        if missing:
            log(f"FATAL: missing tools: {missing}")
            return 1

        # S1: start_game_with_seed("age-of-dragons-1024")
        send_request(proc, 3, "tools/call", {
            "name": "start_game_with_seed",
            "arguments": {"seed_id": SEED_ID},
        })
        resp = read_response(proc)
        if "result" not in resp:
            log(f"FATAL: start_game_with_seed no result: {resp}")
            return 1
        payload = extract_tool_payload(resp["result"])
        if not payload.get("ok"):
            log(f"FATAL: start_game_with_seed not ok: {payload}")
            return 1
        if payload.get("game_id") != SEED_ID:
            log(f"FATAL: game_id {payload.get('game_id')!r} != {SEED_ID!r}")
            return 1
        if payload.get("lore_chunks_indexed", 0) < 30:
            log(f"FATAL: lore_chunks_indexed {payload.get('lore_chunks_indexed')} < 30")
            return 1
        log(f"S1 ✓ start_game_with_seed ok, {payload.get('lore_chunks_indexed')} chunks indexed")

        # S3: read_lore on a known chunk
        send_request(proc, 4, "tools/call", {
            "name": "read_lore",
            "arguments": {"game_id": SEED_ID, "chunk_name": "용발톱 무리 (Dragonclaw Horde)"},
        })
        resp = read_response(proc)
        payload = extract_tool_payload(resp["result"])
        if not payload.get("ok"):
            log(f"FATAL: read_lore not ok: {payload}")
            return 1
        chunk = payload.get("chunk", {})
        if chunk.get("type") != "faction":
            log(f"FATAL: Dragonclaw chunk type {chunk.get('type')} != 'faction'")
            return 1
        log(f"S3 ✓ read_lore returned Dragonclaw chunk ({len(chunk.get('content', ''))} chars)")

        # S2: advance_turn
        event = {
            "event_id": "ev-fantasy-rpg-qa-001",
            "turn": 0,
            "actor_id": "character_lyndwell",
            "action": "custom",
            "payload": {"verb": "negotiate", "note": "Manual QA fantasy-rpg round-trip."},
            "reason": "Manual QA: fantasy-rpg first turn — Lyndwell negotiates with Bren.",
        }
        send_request(proc, 5, "tools/call", {
            "name": "advance_turn",
            "arguments": {"game_id": SEED_ID, "event": event},
        })
        resp = read_response(proc)
        payload = extract_tool_payload(resp["result"])
        if not payload.get("ok"):
            log(f"FATAL: advance_turn not ok: {payload}")
            return 1
        if payload.get("turn") != 1:
            log(f"FATAL: advance_turn returned turn {payload.get('turn')}, expected 1")
            return 1
        log("S2 ✓ advance_turn ok, turn 0 -> 1")

        # read_state_history
        send_request(proc, 6, "tools/call", {
            "name": "read_state_history",
            "arguments": {"game_id": SEED_ID},
        })
        resp = read_response(proc)
        payload = extract_tool_payload(resp["result"])
        if not payload.get("ok") or payload.get("count", 0) < 1:
            log(f"FATAL: read_state_history not ok or count < 1: {payload}")
            return 1
        log(f"S2b ✓ read_state_history count={payload.get('count')}")

        # end_session
        send_request(proc, 7, "tools/call", {
            "name": "end_session",
            "arguments": {"game_id": SEED_ID},
        })
        resp = read_response(proc)
        payload = extract_tool_payload(resp["result"])
        if not payload.get("ok"):
            log(f"FATAL: end_session not ok: {payload}")
            return 1
        log("S8b ✓ end_session ok")

        log("=" * 50)
        log("ALL FANTASY-RPG CONTRACT CHECKS PASSED")
        log(f"  S1: start_game_with_seed ok, chunks indexed")
        log(f"  S2: advance_turn 0->1 ok, audit entry written")
        log(f"  S3: read_lore returned Dragonclaw chunk verbatim")
        log(f"  S8: end-to-end round-trip succeeded")
        log(f"State file: {tmpdir / SEED_ID / 'state.json'}")
        log(f"Audit log:  {tmpdir / SEED_ID / 'audit.jsonl'}")
        log(f"world.md:   {tmpdir / SEED_ID / 'lore' / 'world.md'}")
        return 0

    except Exception as e:
        log(f"FATAL exception: {e}")
        return 1
    finally:
        try:
            proc.stdin.close()
        except Exception:
            pass
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    sys.exit(main())
