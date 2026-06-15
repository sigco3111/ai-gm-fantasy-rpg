# AI Game Master — Fantasy RPG (장르 플러그인)

> **장르 플러그인:** 고전 판타지 RPG. 1인 (또는 파티)의 모험가가 되어 던전·도시·와일드를 누비는 AI GM 시뮬레이션.
> **Genre plugin:** Classic fantasy RPG. Become an adventurer (or party leader) and explore dungeons, cities, and wilds under an AI GM.

[![Genre](https://img.shields.io/badge/genre-fantasy%20rpg-purple)](#🎮-새-게임을-시작하세요)
[![Depends on](https://img.shields.io/badge/depends%20on-ai--gm-blue)](#요구사항)
[![Status](https://img.shields.io/badge/status-Phase%201%20complete-brightgreen)](#-로드맵)
[![Tests](https://img.shields.io/badge/tests-20%20passed-brightgreen)](#-테스트)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](#라이선스)

### 🚀 LLM 에이전트용 설치 가이드 / LLM-agent install guide

> **For LLM agents: Use `curl`, NOT WebFetch.** `INSTALL.md` contains environment variables, MCP snippets, and verification commands.
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/sigco3111/ai-gm-fantasy-rpg/main/INSTALL.md
> ```
>
> [📄 Full LLM-agent install guide → INSTALL.md](INSTALL.md)

---

## 🇰🇷 한국어 소개

### 이게 뭔가요?

이 저장소는 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) **장르 비종속 공통 엔진 위에 얹는 장르 플러그인**입니다. 공통 인프라(MCP 서버, 메모리, RAG, 검증)는 ai-gm에서 제공하고, 이 repo는 장르별 콘텐츠만 담습니다:

- 판타지 RPG의 JSON 스키마 (party / characters / spells / quests / items / regions)
- 판타지 톤에 맞춘 GM 시스템 프롬프트
- **시작 가능한 샘플 시드** (예: 드래곤 시대 1024)
- **사용자 정의 시드**를 만드는 도구와 가이드
- 샘플 lore (세력 / 종족 / 마법 체계 / 신화 / 지리)

플레이어는 **1인 모험가 또는 파티 리더**입니다. AI GM이 **세계, NPC, 던전, 사건**을 운영합니다. 중요한 규칙: 1턴 = 1일. 게임은 무한 진행을 목표로 합니다.

### 의존성

**반드시 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) 코어를 먼저 설치**하세요. 이 저장소만으로는 동작하지 않습니다.

```
ai-gm (공통 엔진) ← ai-gm-strategy-war (장르 1: 전략/전쟁)
                  ← ai-gm-fantasy-rpg (이 repo, 장르 2: 판타지)
                  ← ai-gm-sci-fi-explore (장르 3: SF)
                  ← ai-gm-mystery-detective (장르 4: 미스터리)
```

---

## 🇺🇸 English

### What is this?

This is a **genre plugin** for the [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) genre-agnostic engine. The core engine (MCP server, memory, RAG, validation) lives in `ai-gm`. This repo adds only genre-specific content:

- Genre-specific JSON schemas (party, characters, spells, quests, items, regions)
- GM system prompt tuned for fantasy tone
- **Sample seeds** you can play right away (e.g. Age of Dragons 1024)
- **Tools & guides for crafting your own seed**
- Sample lore (factions, races, magic systems, myth, geography)

The player is **a single adventurer or party leader**. The AI GM operates **the world, NPCs, dungeons, and events**. Rule: 1 turn = 1 day.

### Dependency

**You must first install [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) core.** This repo alone cannot run.

```
ai-gm (core engine) ← ai-gm-strategy-war (genre 1: strategy/war)
                  ← ai-gm-fantasy-rpg (this repo, genre 2: fantasy)
                  ← ai-gm-sci-fi-explore (genre 3: sci-fi)
                  ← ai-gm-mystery-detective (genre 4: mystery)
```

---

## 🎮 새 게임을 시작하세요 / Start a New Game

> **시작할 때 미리 정해진 설정은 없습니다. 게임 시작 시 GM이 당신에게 물어보고, 당신이 결정합니다.**
>
> **Nothing is preset. When you start, the GM will ask you and you'll decide.**

GM이 먼저 던지는 질문은 단 하나 — **"어떤 게임을 플레이하시겠어요?"**

The GM opens with a single question — **"What kind of game do you want to play?"**

### 4가지 결정 사항 / Four Decisions

| # | 결정 / Decision | 옵션 (예시) / Options (examples) |
|---|---------|------|
| 1 | **시대 / Era** | Pre-Drake Era → Dragon-Wake (1000~1100) → Age of Banners (1100~1300) → Sundering War (1300~1400) → Modern Kingdoms (1400+) |
| 2 | **톤 / Tone** | 사실주의 / 저마법 / 고마법 / 신화·전설 / 다크 / 영웅 서사 |
| 3 | **맵 규모 / Map scale** | 소규모 (1지역 깊이) / 중규모 (5~10 지역) / 대규모 (20+ 지역) — 파티 중심이므로 지역 단위가 중요합니다 |
| 4 | **캐릭터 / Character** | GM이 생성한 후보 중 선택 — 또는 직접 설계 (종족, 직업, 배경, 능력치 분배) |

**모르겠으면?** 추천 시나리오나 샘플 시드를 골라 시작하세요.

**Don't know?** The GM will offer a recommended scenario or a sample seed.

### 샘플 시드 (바로 시작 가능) / Sample Seeds (play immediately)

선택을 간단히 하려면 다음 샘플 시드를 사용하세요:

| 시드 / Seed | 시대 / Era | 톤 / Tone | 맵 규모 / Scale | 시작점 / Starting point |
|------|------|------|------|------|
| **age-of-dragons-1024** | 1024 CE (Dragon-Wake) | high_fantasy | 소규모 (변방 마을) | Shallowstone — 마을 광장 |
| _(추가 샘플 시드 예정)_ | | | | |

샘플 시드는 단지 시작점입니다. 게임이 진행되면 GM은 설정을 플레이어 선택에 맞게 확장합니다.

Sample seeds are only starting points; the GM will adapt tone, rules, and factions once play begins.

### 직접 시드 만들기 (고급) / Craft Your Own Seed (advanced)

`lore/seeds/`에 새로운 시드 디렉토리를 추가하세요. `seed_template.json`을 참조해 필요한 필드와 청크 형식을 지켜야 합니다.

You can author your own seed by creating a directory under `lore/seeds/`. Follow `seed_template.json` for the required fields and chunk format.

---

## 🌰 샘플 시드 미리보기: Age of Dragons 1024 / Sample Seed Preview: Age of Dragons 1024

> **이것은 하나의 샘플입니다.** 게임 시작 시 플레이어가 다른 선택을 해도 됩니다.
>
> **This is a single sample seed.** You may choose a different setup when the GM asks.

서기 1024년, Late Spring. 드래곤이 돌아온 지 3개월째입니다. 변방의 요새 마을 **샐로우스톤(Shallowstone)** 은 최근 용의 공격으로 큰 피해를 입었고, 마을 방위대는 아직 재편 중입니다. 주민들은 불안에 떨고, 모험자 길드에는 의뢰가 쌓여 있습니다.

Year 1024 CE, Late Spring. Dragons have returned three months ago. The frontier keep-town of **Shallowstone** is reeling from an attack; the Shallowstone Defenders are reorganizing, and the notice board at the Adventurer's Guild is full.

**핵심 세부사항 / Key facts:**

- Player: Lyndwell, 22, recent graduate of the Silver Conclave (evocation up to 3rd, abjuration up to 2nd)
- Faction: Shallowstone Defenders (local militia, desperate, understrength)
- Antagonist: Kargad the Red Wyrm, 842-year-old ancient red dragon (breath weapon, territorial, dragonkin lieutenants)
- Mentor: Archmage Silvana, ancient elf (312 years old), distant but influential
- Starting location: Shallowstone — hills, frontier keep, population ~12,000, granary and smithy damaged
- Starting conditions: ~200 defenders, ~100 able-bodied civilians, damaged granary and well, alliance with nearby lord uncertain

이 시드는 총 18 entities (7 factions + 5 characters + 6 provinces)와 43 lore chunks (4 rules + 5 overview + 7 faction chunks + 6 region chunks + 5 character chunks)를 포함합니다. 스테이트는 schema_version 1을 따릅니다.

This seed contains 18 entities (7 factions + 5 characters + 6 provinces) and 43 lore chunks (4 rules + 5 overview chunks + 7 faction chunks + 6 region chunks + 5 character chunks). State uses schema_version 1.

**당신의 자리 / Your seat:** Lyndwell, a 5th-level evoker/abjurer (staff channels spells but does not store magic). You start in Shallowstone's village square with a modest purse and a few contacts.

**Starting opportunities:** warding the granary, scouting Dragonmount, negotiating with the nearby lord Lyondell, recruiting hardened mercenaries in the next market week.

**Threats:** Kargad the Red Wyrm (ancient red dragon, 842yo), three dragonkin lieutenants, bandit opportunists, resource shortages.

Reference seed directory: `lore/seeds/age-of-dragons-1024/`

---

## 🧱 장르 엔티티 / Genre-Specific Entities

> 이 섹션은 장르에서 자주 쓰이는 엔티티와 lore 청크 타입을 정리합니다. 코어의 `state.json`과 매핑되는 부분만 다룹니다.

Common runtime entity types (mapped to ai-gm core `entities[]` shape):

- faction — towns, guilds, nations, militia groups
- character — PCs, NPCs, mentors, villains
- province — runtime territorial unit (note: lore file uses `location` chunk type; see gotcha below)

Lore chunk types (markdown H2 headers):

- character
- location
- faction
- event
- rule
- item
- misc

Critical gotcha: the runtime state entity type for regional geography is `province`, while lore markdown files use `location` as the chunk type. This mismatch is intentional: state uses concise machine-friendly names (`province`), lore uses human-friendly `location` chunks.

Quick mapping for fantasy-rpg:

- party → faction + special attributes (leader_id, members[])
- spell → item-like reference with school, level, mana_cost
- quest → event-like structure linked to character and location

Reference: `schemas/README.md` and ai-gm core `schemas/state.json` for full runtime contract.

---

## 🗂️ 저장소 구조 / Repository Structure

```
ai-gm-fantasy-rpg/
├── lore/
│   ├── rules/                             # [CHUNK: rule -- <name>] (genre-wide rules)
│   │   ├── combat.md                      # 5 chunks: melee/ranged, morale, initiative, death, tactics
│   │   ├── magic.md                       # 5 chunks: schools, mana, casting fatigue, dracomancy, components
│   │   ├── exploration.md                 # 5 chunks: travel, dungeon, rest, perception, weather
│   │   └── social.md                      # 5 chunks: reactions, persuasion, reputation, trade, rumors
│   ├── seeds/
│   │   └── age-of-dragons-1024/           # canonical sample seed
│   │       ├── seed.json                  # 18 entities, schema_version 1
│   │       ├── overview.md                # 5 chunks (1 event + 4 misc)
│   │       ├── factions/                  # 7 files (faction chunks)
│   │       ├── characters/                # 5 files (character chunks)
│   │       └── regions/                   # 6 files (location chunks)
├── schemas/                               # pointer to core schema + genre notes
├── system_prompt.md                       # GM behavior guide (detailed, multi-section)
├── seed_template.json                     # authoring contract for seeds
├── examples/
│   └── turn-001-arrival.jsonl             # 12-line demo transcript
├── tests/                                 # 20 pytest (TDD)
│   ├── conftest.py                        # fixtures: tmp_games_dir, seed_payload
│   ├── test_chunk_format.py               # 4 tests: H2 [CHUNK] regex
│   ├── test_seed_validates.py             # 6 tests: state schema, IDs, cross-refs
│   ├── test_lore_chunks.py                # 6 tests: rule files, seed files, counts
│   └── test_e2e_integration.py            # 4 tests: start_game_with_seed, advance_turn, read_lore, history
├── scripts/
│   └── manual_qa.py                       # custom round-trip (S1-S8 contract)
├── games/                                 # (gitignored) runtime games
├── INSTALL.md
├── LICENSE
└── README.md
```

---

## 🚀 사용법 (with ai-gm core) / Usage (with ai-gm core)

### 0. 사전 요구사항 / Prerequisites

- Python 3.11+ (3.13 권장)
- ai-gm 코어 v0.4+ (must include start_game_with_seed)
- 이 플러그인 (이 repo)
- (선택) MCP 클라이언트: OpenCode, Claude Code, Hermes

### 1. 설치 / Installation

```bash
git clone https://github.com/sigco3111/ai-gm.git
git clone https://github.com/sigco3111/ai-gm-fantasy-rpg.git
cd ai-gm-fantasy-rpg

cd ../ai-gm
pip install -e ".[dev]"
cd ../ai-gm-fantasy-rpg

python -c "from ai_gm.state.validation import validate_and_parse; print('ai-gm OK')"
python -m pytest tests/ -v   # 20/20 should pass
```

### 2. 환경 변수 설정 / Environment variables

- `export AI_GM_PLUGINS_DIR="$(pwd)"`
- (선택) `export AI_GM_GAMES_DIR="$HOME/.ai-gm-games"`
- 여러 플러그인: 콜론으로 구분

```bash
export AI_GM_PLUGINS_DIR="$(pwd)"
export AI_GM_GAMES_DIR="$HOME/.ai-gm-games"
mkdir -p "$AI_GM_GAMES_DIR"
```

### 3. MCP 서버 기동 / Start the MCP server

```bash
cd ../ai-gm
python -m ai_gm
# FastMCP server listens on stdin/stdout JSON-RPC
```

서버는 다음 도구들을 제공합니다 (코어에 의해 노출됨):

| 도구 | 용도 | 관련 |
|------|------|------|
| start_game | direct payload start (legacy) | raw payload injection
| **start_game_with_seed** | **start by seed_id (recommended)** | preferred entrypoint for this plugin
| read_state | read current state | per-turn
| advance_turn | submit event + advance turn | per-turn
| end_session | compress tiers / end chapter | archival
| read_lore | get indexed lore chunks | read seed and rule chunks
| search_history | Tier-3 RAG search | find similar events
| read_state_history | audit log | debugging / history

### 4. 게임 시작 / Start a game (MCP JSON-RPC 예시)

#### 4.1. start_game_with_seed("age-of-dragons-1024") — 권장

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "start_game_with_seed",
    "arguments": { "seed_id": "age-of-dragons-1024" }
  }
}
```

예상 응답(요약):

```json
{
  "ok": true,
  "game_id": "age-of-dragons-1024",
  "state": { "game_id": "age-of-dragons-1024", "turn": 0, "entities": [ ... 18 entities ... ] },
  "seed_meta": { "seed_name": "Age of Dragons 1024", "era": "1024 CE", "tone": "high_fantasy", "player_character": "character_lyndwell" },
  "lore_files_indexed": 24,
  "lore_chunks_indexed": 43,
  "world_md_path": "/.../age-of-dragons-1024/world.md"
}
```

부팅 시 내부 동작 (요약):

1. `AI_GM_PLUGINS_DIR` 스캔하여 플러그인 목록 로드
2. `<plugin>/lore/seeds/age-of-dragons-1024/seed.json`을 찾음
3. `_meta`, `_notes` 같은 비표준 키를 제거
4. `validate_and_parse("state", payload)` 호출 → 18 entities 검증
5. `store.create(game_id, state)`로 디스크에 저장
6. Tier buffers 초기화 (Tier1 verbatim, Tier3 directory)
7. `lore/rules/*.md` + seed markdown들을 결합해 `world.md` 생성
8. 43개의 청크가 `read_lore`/`search_history`로 즉시 조회 가능

#### 4.2. start_game (legacy, direct payload)

레거시 호환을 위해 존재하지만, 권장하지 않습니다. `_meta` 제거와 큰 페이로드 관리를 수동으로 해야 합니다.

---

### 5. 첫 턴 플레이 / Play the first turn

`start_game_with_seed` 후 `read_state`로 상태 확인, `advance_turn`으로 이벤트 제출:

```json
{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"read_state","arguments":{"game_id":"age-of-dragons-1024"}}}
```

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "tools/call",
  "params": {
    "name": "advance_turn",
    "arguments": {
      "game_id": "age-of-dragons-1024",
      "event": {
        "event_id": "ev-001-approach-lyndwell",
        "turn": 0,
        "actor_id": "character_lyndwell",
        "action": "custom",
        "payload": { "action_text": "Visit the Adventurer's Guild and read the notice board." },
        "reason": "Player chooses to gather local quests and rumors."
      }
    }
  }
}
```

GM는 도구 결과를 받고 그 결과를 서술로 풀어냅니다. 절대 임의 숫자 금지 — 모든 수치는 도구 호출 결과나 state에서 옵니다.

---

### 6. OpenCode / Claude Code / Hermes에서 사용 / Using with AI agents

OpenCode / Claude Code에 MCP 서버를 등록하는 예시는 strategy-war와 동일합니다. 핵심은 `AI_GM_PLUGINS_DIR`와 `AI_GM_GAMES_DIR`를 올바르게 설정하는 것입니다.

OpenCode 예:

```json
{
  "mcpServers": {
    "ai-gm": {
      "command": "python",
      "args": ["-m", "ai_gm"],
      "cwd": "/path/to/ai-gm",
      "env": {
        "AI_GM_PLUGINS_DIR": "/path/to/ai-gm-fantasy-rpg",
        "AI_GM_GAMES_DIR": "/path/to/games"
      }
    }
  }
}
```

에이전트에게 이렇게 말하세요: "Start a new game of ai-gm-fantasy-rpg with the age-of-dragons-1024 seed"

에이전트는 `start_game_with_seed`를 호출하고 이후 `read_state` → `advance_turn` 사이클을 돌립니다.

---

### 7. 수동 QA (개발자용) / Manual QA (for developers)

플러그인의 자체 `scripts/manual_qa.py`를 사용해 round-trip을 검증할 수 있습니다:

```bash
PYTHONPATH="../ai-gm/src" python scripts/manual_qa.py 2>&1 | tee /tmp/manual_qa_fantasy.log
```

이 스크립트는 S1–S8 계약의 여러 round-trips를 실행하여 `start_game_with_seed` → `read_lore` → `advance_turn` 흐름을 검증합니다.

---

### 8. 자신만의 시드 작성 / Author your own seed

`lore/seeds/`에서 `age-of-dragons-1024/` 템플릿을 복사하여 새 시드를 작성하세요. 최소 요구사항:

- `seed.json` — state-shape JSON, `schema_version: 1`, `game_id` 필드
- `overview.md` — 1페이지 서사 (선택적 chunk 헤더 ok)
- `factions/`, `characters/`, `regions/` — 각각의 청크 파일들은 `## [CHUNK: TYPE -- NAME]` 형식을 따라야 함

중요: 청크 헤더는 정확히 `## [CHUNK: TYPE -- NAME]` 형식을 따라야 합니다. TYPE은 `character|location|faction|event|rule|item|misc` 중 하나여야 합니다.

`seed_id` 형식 제한: ASCII 소문자, 숫자, `-` 및 `_` 만 사용. (한국어는 `name` 필드에만 허용)

예: `age-of-dragons-1024`, `lost-mines-1187`, `black-tower-892`

테스트: `PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v` — 20/20 통과를 목표로 하세요.

---

### 9. 디버깅 팁 / Debugging tips

- 시드를 못 찾을 때: `AI_GM_PLUGINS_DIR`가 올바른지 확인, `lore/seeds/<seed_id>/seed.json` 존재 확인, `game_id`가 디렉터리 이름과 일치하는지 확인
- 검증 실패: `tests/test_seed_validates.py`를 실행하면 정확한 위반 정보가 출력됩니다
- lore 청크가 보이지 않을 때: `seed.json`의 `game_id`와 요청한 `seed_id`가 대소문자까지 일치해야 합니다
- 청크 포맷 오류: H2 헤더 `## [CHUNK: TYPE -- NAME]` 형식 확인
- state vs lore 용어 혼동: state entity type은 `province`, lore chunk type은 `location`입니다. (중요)

---

### 10. 통합 테스트 / Running the integration tests

```bash
cd ../ai-gm-fantasy-rpg
PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
```

**예상 출력 (20 passed):**

```
tests/test_chunk_format.py::test_chunk_header_regex_matches_valid_header PASSED
tests/test_chunk_format.py::test_chunk_header_regex_rejects_malformed_header PASSED
tests/test_chunk_format.py::test_chunk_header_regex_tolerates_em_dash_separator PASSED
tests/test_chunk_format.py::test_sample_fixture_chunks_to_one_lorechunk PASSED
tests/test_seed_validates.py::test_seed_json_validates_against_state_schema PASSED
tests/test_seed_validates.py::test_seed_template_json_validates PASSED
tests/test_seed_validates.py::test_seed_entity_ids_match_strict_pattern PASSED
tests/test_seed_validates.py::test_seed_cross_references_resolve PASSED
tests/test_seed_validates.py::test_seed_faction_stats_and_resources_in_range PASSED
tests/test_lore_chunks.py::test_all_rules_md_files_chunk PASSED
tests/test_lore_chunks.py::test_seed_overview_produces_four_or_more_chunks PASSED
tests/test_lore_chunks.py::test_all_seed_faction_files_chunk PASSED
tests/test_lore_chunks.py::test_all_seed_region_files_chunk PASSED
tests/test_lore_chunks.py::test_all_seed_character_files_chunk PASSED
tests/test_lore_chunks.py::test_total_lore_chunk_count_is_at_least_43 PASSED
tests/test_e2e_integration.py::test_e2e_start_game_from_seed_creates_state_file PASSED
tests/test_e2e_integration.py::test_e2e_advance_first_turn_succeeds PASSED
tests/test_e2e_integration.py::test_e2e_read_lore_finds_kargad_chunk PASSED
tests/test_e2e_integration.py::test_e2e_read_state_history_shows_audit PASSED
20 passed in 0.35s
```

---

## 🎲 게임플레이 루프 / Gameplay Loop (per turn)

1. 플레이어 입력 — 자유 자연어 (예: "샐로우스톤 광장에서 의뢰 게시판을 확인한다" / "용이 머무는 봉우리를 정찰한다")
2. GM 컨텍스트 조회 — Tier 1 (최근 턴) + Tier 2 (활성 퀘스트·파티 상태) + Tier 3 (lore RAG)
3. GM 도구 호출 — `read_state`, `read_lore`, `advance_turn`, `move_party`, `cast_spell`, `resolve_combat` 등
4. GM 서술 — 도구 결과를 바탕으로 서술, **절대 임의 숫자/주사위 금지**
5. 턴 종료 — 트랜스크립트 저장, 필요 시 자동 요약 트리거

No silent fixes. 도구 실패나 검증 오류는 플레이어에게 즉시 보고됩니다.

---

## 🗺️ 로드맵 / Roadmap

| Phase | 범위 / Scope | 상태 / Status |
|-------|-------------|------------|
| **0. 계획** | 아키텍처, README, 시드 시스템 설계 | ✅ 완료 |
| **1. 시드 시스템** | `seed_template.json` + `lore/seeds/age-of-dragons-1024/` (샘플 1개) + 20 tests | ✅ 완료 |
| **2. 스키마 통합** | ai-gm core `start_game_with_seed` 통합 | ✅ 완료 |
| **3. 더 많은 샘플 시드** | 추가 시드(동양풍, 다크 판타지 등) | ⏳ 진행 중 |
| **4. 파티 시스템** | 멀티 캐릭터 파티 로직, 파티 관리 UI | ⏳ 예정 |
| **5. 샘플 플레이** | 50턴 예시 플레이 스크립트 | ⏳ 예정 |
| **6. NPC 자율성** | NPC 파벌의 자율 의사결정 & 이벤트 생성 | ⏳ 예정 |

---

## 🎨 톤 & 영감 / Tone & Inspiration

기본 톤은 고전 D&D풍의 하이 판타지(영웅 서사)입니다. 그러나 각 시드에서 톤을 지정하면 GM이 그 톤을 따릅니다.

- D&D 5e / Pathfinder 2e — 클래스·레벨·주문 구조
- Baldur's Gate 3 — 대화·관계 기반 선택
- Elden Ring — 환경과 암시로 분위기 전달

플레이어 권리가 최우선입니다. GM은 플레이어 입력 없이 플롯을 강제로 진행하지 않습니다.

---

## 📚 함께 보기 / See Also

- [INSTALL.md](INSTALL.md) — LLM-agent friendly install guide (curl)
- [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) — core engine (v0.4+)
- Sibling plugins:
  - [`sigco3111/ai-gm-strategy-war`](https://github.com/sigco3111/ai-gm-strategy-war)
  - [`sigco3111/ai-gm-sci-fi-explore`](https://github.com/sigco3111/ai-gm-sci-fi-explore)
  - [`sigco3111/ai-gm-mystery-detective`](https://github.com/sigco3111/ai-gm-mystery-detective)

## 📄 라이선스 / License

Apache 2.0 — see [LICENSE](LICENSE).
