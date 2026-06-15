# AI Game Master — Fantasy RPG (장르 플러그인)

> **장르 플러그인:** 고전 판타지 RPG. 1인 (또는 파티)의 모험가가 되어 던전·도시·와일드를 누비는 AI GM 시뮬레이션.
> **Genre plugin:** Classic fantasy RPG. Become an adventurer (or party leader) and explore dungeons, cities, and wilds under an AI GM.

[![Genre](https://img.shields.io/badge/genre-fantasy%20rpg-purple)](#🎮-새-게임을-시작하세요)
[![Depends on](https://img.shields.io/badge/depends%20on-ai--gm-blue)](#요구사항)
[![Status](https://img.shields.io/badge/status-Phase%201%20complete-brightgreen)](#-로드맵)
[![Tests](https://img.shields.io/badge/tests-20%20passed-brightgreen)](#-테스트)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](#라이선스)

---

## 🇰🇷 한국어 소개

### 이게 뭔가요?

이 저장소는 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) **장르 비종속 공통 엔진 위에 얹는 장르 플러그인**입니다. 공통 인프라(MCP 서버, 메모리, RAG, 검증)는 ai-gm에서 가져오고, 이 repo는 장르 콘텐츠만 담습니다:

- 판타지 RPG의 JSON 스키마 (party / characters / spells / quests / items / regions)
- 판타지 톤에 맞춘 GM 시스템 프롬프트
- **시작 가능한 샘플 시드** (예: 드래곤 시대의 변방 왕국)
- **사용자 정의 시드**를 만드는 도구와 가이드
- 샘플 lore (세력 / 종족 / 마법 체계 / 신화 / 지리)

플레이어는 **1인 모험가 또는 파티 리더**. AI GM이 **세계, NPC, 던전, 사건**을 운영합니다. 1턴 = 1일, 무한 진행.

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
- **Sample seeds** you can play right away (e.g. a border kingdom in the Age of Dragons)
- **Tools & guides for crafting your own seed**
- Sample lore (factions, races, magic systems, myth, geography)

The player is **a single adventurer or party leader**. The AI GM operates **the world, NPCs, dungeons, and events**. 1 turn = 1 day, infinite progression.

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
| 1 | **서브 장르** / **Sub-genre** | 고전 D&D풍 (용·마법·던전) / 다크 판타지 (위험한 마법) / 무마법 (저마법, 현실적) / 동양풍 (검협·선인) / 모더니즘 (현대 도시+마법) |
| 2 | **톤** / **Tone** | 영웅 서사 / 다크·험오 / 코미디 / 비극 / 코지 (힐링) / 단편집풍 (한 판 = 한 사건) |
| 3 | **스케일** / **Scale** | 소규모 (1왕국 깊이, 던전 위주) / 중규모 (대륙 일부, 여러 왕국) / 대규모 (대륙 전체, 종족/신들 관여) |
| 4 | **당신의 캐릭터** / **Your character** | 종족(인간/엘프/드워프/하프링/오크/티플링/...) + 직업(전사/마법사/도적/성직자/바드/...) — GM이 가이드 |

**모르겠으면?** GM이 "추천 빌드"를 제시하거나, 샘플 시드를 추천해줍니다.

**Don't know?** The GM will offer a "recommended build" or point you to a sample seed.

### 샘플 시드 (바로 시작 가능) / Sample Seeds (play immediately)

미리 만들어진 시드 중 골라도 됩니다 — 결정 4가지를 한 번에 단축:

| 시드 / Seed | 서브장르 / Sub-genre | 톤 / Tone | 스케일 / Scale | 시작점 / Starting point |
|------|------|------|------|------|
| **드래곤 시대 1024** (Age of Dragons 1024) | 고전 D&D풍 | 영웅 서사 | 소규모 | 변방 마을 "샐로우스톤" — 용의 습격 이후 |
| _(더 많은 샘플 시드 추가 예정)_ | | | | |

샘플 시드는 **그냥 시작점**입니다 — 본게임에 들어서면 톤·규칙·세계관은 GM이 자유롭게 변주할 수 있어요.

Sample seeds are just **starting points** — once the game begins, the GM may freely riff on tone, rules, and world.

### 직접 시드 만들기 (고급) / Craft Your Own Seed (advanced)

`lore/seeds/`에 직접 YAML/JSON을 작성해 완전히 새로운 세계를 던져줄 수도 있습니다. `seed_template.json`을 참고하세요.

You can also drop your own YAML/JSON into `lore/seeds/` to hand the GM a fully custom world. See `seed_template.json` for the schema.

---

## 🌰 샘플 시드 미리보기: 드래곤 시대 1024 / Sample Seed Preview: Age of Dragons 1024

> **이건 *하나의 예시*일 뿐입니다. 위 "새 게임을 시작하세요" 섹션의 옵션으로 당신이 무엇이든 정할 수 있어요.**
>
> **This is *one* example. The "Start a New Game" section above lets you pick anything you want.**

서기 1024년. 알드란드 대륙의 동쪽 변방 — 작은 마을 **샐로우스톤**. 한 달 전, "붉은 비룡" 카르가가 마을 외곽의 목축지를 초토화했습니다. 마을 의뢰가 게시판에 줄을 잇고, 모험자 길드 지부는 초상집에서 썩어갑니다. 당신은 그 지부를 지나던 — 또는 처음 발을 딛는 — 모험가입니다.

Year 1024. The eastern frontier of the Aldrand continent — the village of **Shallowstone**. A month ago, the Red Wyrm **Kargad** scorched the outlying rangelands. The notice board is covered in desperate requests; the Adventurer's Guild outpost sits idle. You are the adventurer passing through — or setting foot for the first time.

**당신의 자리 / Your seat:** 1인 모험가 (또는 최대 4인 파티의 리더). 샐로우스톤 마을 광장.

**Your seat:** a single adventurer (or leader of a party of up to 4). Shallowstone village square.

**시작 조건 / Starting conditions:**
- 클래스 / Class: 자유 선택 (전사/도적/마법사/성직자/바드/... 자유 조합)
- 동료 / Companions: 0~3명 (광장에서 모집 가능)
- 골드 / Gold: 50 (한 끼와 여관 1박)
- 의뢰 / Active quests: 6건 (용 토벌, 납치자 추적, 던전 탐사, 약초 수집, ...)
- 평판 / Reputation: "이름 없는 여행자" (마을에 알려진 바 없음)

전체 시드 파일은 `lore/seeds/age-of-dragons-1024/`에서 확인 (Phase 1 추가).

Full seed files in `lore/seeds/age-of-dragons-1024/` (Phase 1).

---

## 🧱 장르 엔티티 / Genre-Specific Entities

> **이 스키마는 "플레이 가능한 모든 시나리오"의 공통 부분집합입니다.** 시드마다 일부 필드가 추가/오버라이드될 수 있습니다.
>
> **This schema is the common subset of all playable scenarios.** Individual seeds may add or override fields.

```json
{
  "party": {
    "leader": "<character_id>",
    "members": ["<character_id>", "..."],
    "shared_inventory": ["<item_id>", "..."],
    "gold": 0,
    "reputation": {"<faction_id>": -100..+100, "...": "..."}
  },
  "characters": {
    "<character_id>": {
      "name": "...",
      "race": "human|elf|dwarf|halfling|orc|tiefling|...",
      "class": "warrior|rogue|wizard|cleric|bard|ranger|paladin|...",
      "level": 1,
      "stats": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0},
      "hp": 0,
      "spells_known": ["<spell_id>", "..."],
      "traits": ["...", "..."],
      "location": "<region_id>"
    }
  },
  "active_quests": [
    {
      "id": "<quest_id>",
      "name": "...",
      "giver": "<character_id>",
      "objectives": ["...", "..."],
      "status": "active|completed|failed",
      "reward": {"gold": 0, "xp": 0, "items": ["..."]}
    }
  ]
}
```

전체 스키마는 Phase 1에서 `schemas/`에 들어갑니다.

Full schema lives in `schemas/` (Phase 1).

---

## 🗂️ 저장소 구조 / Repository Structure

```
ai-gm-fantasy-rpg/
├── lore/                       # 정적 세계관 + 청크 (Git 추적)
│   ├── rules/                  # [CHUNK: rules] (장르 공통, 핀 고정)
│   │   ├── combat.md
│   │   ├── magic.md
│   │   ├── exploration.md
│   │   └── social.md
│   ├── seeds/                  # 시작 가능한 시드 모음 (각 시드 = 디렉토리)
│   │   ├── age-of-dragons-1024/   # [CHUNK: seed]
│   │   │   ├── seed.json       # 시드 정의
│   │   │   ├── factions/
│   │   │   ├── characters/
│   │   │   ├── regions/
│   │   │   ├── spells/
│   │   │   └── overview.md
│   │   └── _template/          # 새 시드 작성용 템플릿
│   └── _shared/                # 시드 간 공유되는 청크
│
├── schemas/                    # 장르 스키마 (Phase 1)
├── system_prompt.md            # GM 행동 규약
├── seed_template.json          # 새 시드 작성 가이드
├── games/                      # (gitignored) 실제 진행 게임
│   └── .gitkeep
├── examples/                   # 샘플 트랜스크립트
│   └── turn-001-arrival.jsonl
├── LICENSE
└── README.md
```

---

## 🚀 빠른 시작 / Quick Start (목표)

```bash
# 1. 코어 + 이 플러그인 클론 / Clone core + this plugin
git clone https://github.com/sigco3111/ai-gm.git
git clone https://github.com/sigco3111/ai-gm-fantasy-rpg.git

# 2. 코어 설치 / Install core
cd ai-gm && pip install -e ".[dev]" && cd ..

# 3. MCP 서버를 에이전트에 등록 / Register MCP server
#    (OpenCode / Claude Code / Hermes 설정 — ai-gm/docs/ 참조)

# 4. 에이전트에게 / Tell your agent:
#    "Start a new game of ai-gm-fantasy-rpg"
#    → GM이 "어떤 게임을 플레이하시겠어요?" 라고 물어봄
#    → The GM will ask "What kind of game do you want to play?"
```

---

## 🎲 게임플레이 루프 / Gameplay Loop (per turn)

1. **플레이어 입력** — 자유 자연어 (예: "마을 광장의 의뢰 게시판부터 본다" / "동쪽 숲 속 오크 무리를 추적한다")
2. **GM 컨텍스트 조회** — Tier 1 (최근 턴) + Tier 2 (활성 퀘스트, 파티 상태) + Tier 3 (관련 lore RAG)
3. **GM 도구 호출** — `move_party`, `attack`, `cast_spell`, `complete_quest`, `advance_turn` 등
4. **GM 서술** — 도구 결과를 바탕으로 묘사, **절대 임의 주사위/숫자 ❌** (도구가 결정)
5. **턴 종료** — 트랜스크립트 저장, 필요 시 자동 요약 트리거

**No silent fixes.** 도구 실패 시 GM은 플레이어에게 정직하게 알리고 대기.

**No silent fixes.** If a tool fails, the GM tells the player honestly and waits for input.

---

## 🗺️ 로드맵 / Roadmap

| Phase | 범위 / Scope | 상태 / Status |
|-------|-------------|------------|
| **0. 계획** | 아키텍처, README, 시드 시스템 설계 | ✅ 진행 중 |
| **1. 시드 시스템** | `seed_template.json` + `lore/seeds/age-of-dragons-1024/` (샘플 1개) | 🔜 다음 |
| **2. 스키마** | 장르별 JSON 스키마 (ai-gm 코어에 등록) | 🔜 다음 |
| **3. 샘플 시드 2~3** | 시드 옵션 확장 (예: 동양풍 검협, 다크 판타지 등) | ⏳ |
| **4. 시드 빌더 도구** | `start_game` MCP 도구 + 대화형 설정 UI | ⏳ |
| **5. 샘플 플레이** | 50턴 진행 가능한 샘플 | ⏳ |

---

## 🎨 톤 & 영감 / Tone & Inspiration

고전 D&D풍 판타지가 **기본 톤**이지만, 시드에서 다른 톤을 지정하면 GM이 그대로 따릅니다.

- **D&D 5e / Pathfinder 2e** — 클래스, 레벨, 주문 체계
- **Baldur's Gate 3** — 대화·관계·도덕적 선택
- **Elden Ring** — 세계 분위기, 환경 서술

**플레이어 권리가 최우선입니다.** GM은 플레이어 입력 없이 플롯을 진행하지 않습니다. 세계는 *반응*하지 *추진*하지 않습니다.

**Classic D&D-flavored fantasy is the *default* tone** — but if you pick a different tone in the seed, the GM follows your lead.

- **D&D 5e / Pathfinder 2e** — class, level, spell systems
- **Baldur's Gate 3** — dialogue, relationships, moral choices
- **Elden Ring** — world atmosphere, environmental storytelling

**Player agency is paramount.** The GM does not advance the plot without player input. The world *reacts*; it does not *push*.

---

## 📚 함께 보기 / See Also

- [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) — 공통 엔진 / shared engine
- [`sigco3111/ai-gm-strategy-war`](https://github.com/sigco3111/ai-gm-strategy-war) — 장르 1: 전략/전쟁 / Genre 1: strategy/war
- (장르 3) `sigco3111/ai-gm-sci-fi-explore`
- (장르 4) `sigco3111/ai-gm-mystery-detective`
- [ai-gm-architecture.md](https://gist.github.com/sigco3111/) — 풀 디자인 문서 (한글) / full design doc (Korean)

## 📄 라이선스 / License

Apache 2.0 — see [LICENSE](LICENSE).

---

## 🐉 Sample Seed — `age-of-dragons-1024`

A canonical seed ships with this plugin, ready to play:

| Field | Value |
|---|---|
| **Game ID** | `age-of-dragons-1024` |
| **Era** | 1024 CE — dragons return after 3 centuries of absence |
| **Tone** | high_fantasy |
| **Player Character** | Lyndwell, a 22-year-old graduate of the Silver Conclave |
| **Player Faction** | `faction_shallowstone_defenders` |
| **Antagonist** | Kargad the Red Wyrm, an 842-year-old ancient red dragon |
| **Entities** | 7 factions, 5 characters, 6 provinces (18 total) |
| **Lore chunks** | 43 (4 rules + 5 overview + 7 factions + 6 regions + 5 characters) |
| **State schema** | schema_version 1 (matches ai-gm core) |

**To start a game with this seed**:

```python
# via the MCP server
result = start_game_with_seed(seed_id="age-of-dragons-1024")
# → returns state + 43 indexed chunks, no manual payload assembly required
```

**Round-trip verified**: 20/20 pytest + manual_qa round-trip both green. See `scripts/manual_qa.py`.

## ✅ Phase 1 Status (complete)

- [x] Phase 0 — initial commit (skeleton + planning README)
- [x] Phase 1 — content parity with `ai-gm-strategy-war`
  - [x] `seed_template.json` (96 lines, fantasy-rpg genre)
  - [x] `system_prompt.md` (218 lines, 10 sections)
  - [x] `INSTALL.md` (375 lines, LLM-agent-friendly)
  - [x] `schemas/README.md` (points to core schema)
  - [x] `lore/rules/` — 4 rule files (combat, magic, exploration, social), 20 chunks
  - [x] `lore/seeds/age-of-dragons-1024/` — seed.json + overview.md + 18 entity files
  - [x] `examples/turn-001-founding.jsonl` — 12-line demo transcript
  - [x] `tests/` — 20 tests across 4 files (pytest, all pass)
  - [x] `scripts/manual_qa.py` — end-to-end round-trip (passes)

**Phase 2+ (future)**: balanced stat blocks, encounter tables, additional sample seeds, integration with the ai-gm monorepo CI.
