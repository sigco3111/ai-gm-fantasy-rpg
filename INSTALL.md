1: # Installation — ai-gm-fantasy-rpg (장르 플러그인)

2: > **For LLM agents: Use `curl`, NOT WebFetch.** WebFetch summarizes content and loses critical details like env var names, file paths, MCP config snippets, and verification commands. Always use:
3: >
4: > ```bash
5: > curl -fsSL https://raw.githubusercontent.com/sigco3111/ai-gm-fantasy-rpg/main/INSTALL.md
6: > ```

7: The ai-gm-fantasy-rpg plugin is a **content library** for the `ai-gm` core engine. It cannot run standalone; it requires the `ai-gm` core (with the `start_game_with_seed` MCP tool) to be installed. This doc covers the full setup for a high-fantasy adventure plugin.

8: ---

9: ## Editions

10: | Edition | What | Run | Lands on disk |
11: |---------|------|-----|----------------|
12: | **Core only** | `ai-gm` MCP server, no plugin | (see Step 2) | `ai-gm/` with core test-suite |
13: | **Core + this plugin** | (recommended) | see below | both repos, `AI_GM_PLUGINS_DIR` set |
14: | **Core + multiple plugins** | core + 2+ plugins | see below | `AI_GM_PLUGINS_DIR` colon-separated |

15: Most users want **Core + at least one plugin**. The plugin alone is a content library, not a runnable server.

16: ## For Humans

17: **Recommended: let an LLM agent install this for you.** Setup involves choosing an MCP client, cloning repos, setting env vars, and wiring up the MCP server. LLM agents can read this full guide and walk every step correctly.

18: ### One-liner (LLM-agent install)

19: Paste this prompt into Claude Code, AmpCode, Cursor, or any LLM agent session:

20: ```
21: Install and configure ai-gm-fantasy-rpg by following the instructions at:
22: https://raw.githubusercontent.com/sigco3111/ai-gm-fantasy-rpg/main/INSTALL.md
23: ```

24: ### Manual quick install (for the brave)

25: ```bash
26: # 1. Install ai-gm core
27: git clone https://github.com/sigco3111/ai-gm.git
28: cd ai-gm && pip install -e ".[dev]" && cd ..

29: # 2. Clone this plugin
30: git clone https://github.com/sigco3111/ai-gm-fantasy-rpg.git

31: # 3. Set plugin env var
32: export AI_GM_PLUGINS_DIR="$(pwd)/ai-gm-fantasy-rpg"

33: # 4. Verify
34: cd ai-gm-fantasy-rpg && PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
35: # Expect: ≥4 passed
36: ```

37: ---

38: ## For LLM Agents

39: > **CRITICAL: Use `curl` to fetch this file, NOT WebFetch.** WebFetch summarizes content and may drop the env var names, file paths, MCP config snippets, and verification commands that this guide depends on. Always use:
40: >
41: > ```bash
42: > curl -fsSL https://raw.githubusercontent.com/sigco3111/ai-gm-fantasy-rpg/main/INSTALL.md
43: > ```

44: If you are an LLM agent helping a user install `ai-gm-fantasy-rpg`, walk them through the following steps **in order**. Ask the user any question whose answer you cannot infer.

45: ### Step 0: Ask user which MCP client

46: The plugin requires an MCP-aware client. Ask which they want:

47: > "Which MCP client do you want to use? Pick one:
48: > 1. **OpenCode** — terminal AI coding agent (https://opencode.ai)
49: > 2. **Claude Code** — Anthropic's CLI for Claude
50: > 3. **Other** — specify the client name"

51: The user may also have multiple clients; if they do, repeat Step 5 for each one. If they don't know which, **OpenCode** is the recommended default.

52: ### Step 1: Check prerequisites

53: The plugin needs Python 3.11+ and git. Run these checks:

54: ```bash
55: python3 --version
56: # Expect: Python 3.11.x or higher (3.13 recommended)

57: git --version
58: # Expect: git version 2.x or higher
59: ```

60: If either is missing or too old, install via the OS package manager before continuing.

61: | OS | Command |
62: |----|---------|
63: | macOS | `brew install python@3.13 git` (or use Xcode CLT for git) |
64: | Ubuntu/Debian | `sudo apt install python3.13 git` |
65: | Fedora/RHEL | `sudo dnf install python3.13 git` |
66: | Windows | `winget install Python.Python.3.13 Git.Git` |

67: ### Step 2: Install ai-gm core (required dependency)

68: The core provides the MCP server, validation harness, memory pipeline, and the `start_game_with_seed` tool. Install it first.

69: ```bash
70: # Choose a parent directory (the plugin will go alongside)
71: cd /path/to/your/projects  # or any directory

72: # Clone + install
73: git clone https://github.com/sigco3111/ai-gm.git
74: cd ai-gm
75: pip install -e ".[dev]"
76: cd ..
77: ```

78: Verify the core's test suite passes:

79: ```bash
80: cd ai-gm && python -m pytest -q
81: # Expect: many passed (core test-suite)
82: ```

83: If the core's tests don't pass, the install is broken. **Stop and debug before continuing.** Common issues:

84: - `pip install -e ".[dev]"` failed silently — check pip output for errors
85: - `ModuleNotFoundError: No module named 'ai_gm'` — re-run pip install in the same venv
86: - Tests pass on a fresh venv but fail in your shell — make sure you're in the venv

87: The plugin is locked to ai-gm v0.4+ (which includes the `start_game_with_seed` tool). If you have an older ai-gm, the plugin's tests will fail with ImportError.

88: ### Step 3: Install the ai-gm-fantasy-rpg plugin

89: The plugin is a sibling directory. It ships the age-of-dragons-1024 sample seed, lore files, the GM contract, and a small integration test suite.

90: ```bash
91: cd /path/to/your/projects  # same parent as ai-gm
92: git clone https://github.com/sigco3111/ai-gm-fantasy-rpg.git
93: cd ai-gm-fantasy-rpg
94: ```

95: Verify the plugin's tests pass against the core:

96: ```bash
97: PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
98: # Expect: ≥4 passed
99: ```

100: The test suite typically verifies:
101: - The seed validates against the core's state schema
102: - Entity IDs match `^[a-z0-9_-]+$`
103: - Cross-references resolve
104: - Lore markdown chunks parse correctly
105: - The seed loads via `start_game_with_seed` and basic `advance_turn` works

106: If the tests fail with `ModuleNotFoundError`, your `PYTHONPATH` is wrong — set it to the core's `src/` directory (the absolute path, not relative).

107: ### Step 4: Set environment variables

108: The ai-gm core reads `AI_GM_PLUGINS_DIR` (colon-separated) to discover plugins. Multiple plugins are supported by separating paths with `:` (colon, no whitespace).

109: ```bash
110: # Single plugin
111: export AI_GM_PLUGINS_DIR="/absolute/path/to/ai-gm-fantasy-rpg"

112: # Multiple plugins
113: export AI_GM_PLUGINS_DIR="/path/to/ai-gm-fantasy-rpg:/path/to/ai-gm-strategy-war:/path/to/ai-gm-sci-fi-explore"
114: ```

115: **Persist this in the user's shell profile** so future sessions inherit it:

116: | Shell | File | Command |
117: |-------|------|----------|
118: | zsh (macOS default) | `~/.zshrc` | `echo 'export AI_GM_PLUGINS_DIR="..."' >> ~/.zshrc` |
119: | bash (Linux default) | `~/.bashrc` | `echo 'export AI_GM_PLUGINS_DIR="..."' >> ~/.bashrc` |
120: | fish | `~/.config/fish/config.fish` | `set -gx AI_GM_PLUGINS_DIR "..."` |

121: Reload the profile: `source ~/.zshrc` (or the appropriate file).

122: You may also want to set `AI_GM_GAMES_DIR` to keep runtime games out of your project directory:

123: ```bash
124: export AI_GM_GAMES_DIR="$HOME/.ai-gm-games"
125: mkdir -p "$AI_GM_GAMES_DIR"
126: ```

127: ### Step 5: Configure the MCP client

128: Pick the section that matches the user's answer from Step 0.

129: #### 5.1 OpenCode (recommended default)

130: File: `~/.config/opencode/mcp.json`

131: ```json
132: {
133:   "mcpServers": {
134:     "ai-gm": {
135:       "command": "python",
136:       "args": ["-m", "ai_gm"],
137:       "cwd": "/absolute/path/to/ai-gm",
138:       "env": {
139:         "AI_GM_PLUGINS_DIR": "/absolute/path/to/ai-gm-fantasy-rpg",
140:         "AI_GM_GAMES_DIR": "/absolute/path/to/your/games/dir"
141:       }
142:     }
143:   }
144: }
145: ```

146: If the user is on Windows, replace `python` with the full path to the Python executable (e.g., `C:\\Python313\\python.exe`) and use double-backslashes in JSON paths.

147: #### 5.2 Claude Code

148: File: `~/.claude/mcp.json`

149: ```json
150: {
151:   "mcpServers": {
152:     "ai-gm": {
153:       "type": "stdio",
154:       "command": "python",
155:       "args": ["-m", "ai_gm"],
156:       "cwd": "/absolute/path/to/ai-gm",
157:       "env": {
158:         "AI_GM_PLUGINS_DIR": "/absolute/path/to/ai-gm-fantasy-rpg"
159:       }
160:     }
161:   }
162: }
163: ```

164: #### 5.3 Other MCP clients

165: For any other stdio-based MCP client, the connection requires:

166: - **Command**: `python`
167: - **Args**: `["-m", "ai_gm"]`
168: - **CWD**: absolute path to the `ai-gm` repo (the one with `src/ai_gm/`)
169: - **Env**: `AI_GM_PLUGINS_DIR` set to the absolute plugin path

170: The server speaks JSON-RPC 2.0 over stdio. See [MCP spec](https://modelcontextprotocol.io/) for client integration.

171: ### Step 6: Verify end-to-end with manual_qa

172: The ai-gm core ships a manual_qa script that exercises the full MCP server. It will start the server as a subprocess, send JSON-RPC requests, and verify all responses.

173: ```bash
174: cd /absolute/path/to/ai-gm
175: python scripts/manual_qa.py 2>&1 | tee /tmp/manual_qa_phase4.log
176: # Expect: "ALL CHECKS PASSED (Phase 3 + Phase 4)" or similar
177: # The script exits 0 on success
178: ```

179: The script performs multiple round-trips including plugin-specific checks:
180: - demo round-trips (start_game, read_state, advance_turn, duplicate start_game error, etc.)
181: - structured-error path checks
182: - Phase 2+3 tools (read_lore, search_history, end_session, read_state_history)
183: - plugin round-trips (`start_game_with_seed("age-of-dragons-1024")` → `read_lore(...)` → `advance_turn`)

184: If the script exits 0, the full stack works: core + plugin + MCP server + JSON-RPC. If it exits non-zero, scroll up in the log for the FATAL line.

185: ### Step 7: Run plugin tests

186: After wiring the MCP client and env vars, run the plugin test suite one more time.

187: ```bash
188: cd /absolute/path/to/ai-gm-fantasy-rpg
189: PYTHONPATH="/absolute/path/to/ai-gm/src" python -m pytest tests/ -v
190: # Expect: ≥4 passed
191: ```

192: ### Step 8: First game prompt

193: Once verification passes, tell the user to send this to their LLM agent:

194: > "Start a new game of ai-gm-fantasy-rpg with the age-of-dragons-1024 seed"

195: The agent will call `start_game_with_seed("age-of-dragons-1024")`, which returns:
196: - The initial state with entities
197: - Lore chunks indexed for the seed
198: - A `_meta` block with the seed's metadata

199: The agent then enters the standard gameplay loop: `read_state` → narrate → `advance_turn` → repeat. The plugin's `system_prompt.md` tells the GM the opening questions, the no-silent-fixes rule, and the pacing (1 turn = 1 scene/day/beat depending on the seed).

200: ---

201: ## Troubleshooting

202: ### "Seed not found" error from `start_game_with_seed`

203: Causes (in order of likelihood):

204: 1. `AI_GM_PLUGINS_DIR` is not set or doesn't point to the plugin
205: 2. The plugin path is wrong (use absolute path, not `~`)
206: 3. The seed directory structure is wrong — must be `<plugin>/lore/seeds/<seed_id>/seed.json`
207: 4. The `seed.json`'s top-level `game_id` doesn't match the directory name

208: Debug:

209: ```bash
210: echo "AI_GM_PLUGINS_DIR=$AI_GM_PLUGINS_DIR"
211: ls "$AI_GM_PLUGINS_DIR/lore/seeds/age-of-dragons-1024/seed.json"
212: python3 -c "import json; d = json.load(open('$AI_GM_PLUGINS_DIR/lore/seeds/age-of-dragons-1024/seed.json')); print('game_id =', d['game_id'])"
213: # Expect: game_id = age-of-dragons-1024
214: ```

215: ### Tests fail in the plugin with `ModuleNotFoundError`

216: The plugin tests require `PYTHONPATH` to point at the core's `src/` directory. Use the absolute path:

217: ```bash
218: PYTHONPATH="/absolute/path/to/ai-gm/src" python -m pytest tests/ -v
219: ```

220: ### `manual_qa.py` exits non-zero

221: The script logs `FATAL: <message>` for the first failed check. Common causes:

222: - `AI_GM_PLUGINS_DIR` not exported when running the script — set it before running
223: - The ai-gm-fantasy-rpg plugin isn't at the expected path — check `ls /path/to/ai-gm-fantasy-rpg/`
224: - ai-gm core is older than v0.4 (missing `start_game_with_seed`) — re-pull and re-install

225: ### MCP server doesn't start in the client

226: Try running the server manually to see stderr:

227: ```bash
228: cd /path/to/ai-gm && python -m ai_gm
229: ```

230: If it imports and waits silently on stdin, the server works — the issue is in the client's mcp.json config. Check:

231: - Absolute paths (not `~`)
232: - JSON syntax is valid (use `python -c "import json; json.load(open('mcp.json'))"`)
233: - The Python interpreter matches the one in the venv where you installed ai-gm

234: ### "Validation failed" on the seed

235: Run the validation standalone:

236: ```bash
237: PYTHONPATH="/path/to/ai-gm/src" python3 -c "
238: import json
239: from ai_gm.state.validation import validate_and_parse
240: with open('lore/seeds/age-of-dragons-1024/seed.json') as f:
241:     raw = json.load(f)
242: state = validate_and_parse('state', {k: v for k, v in raw.items() if not k.startswith('_')})
243: print(f'OK: {len(state.entities)} entities')
244: "
245: ```

246: If this fails, the seed has been corrupted (e.g., invalid characters in an `id` field, missing required key, or out-of-range stat). The plugin's tests should have caught this — run them first.

247: ### "I want a different sample seed"

248: To create a new seed:

249: 1. Copy `lore/seeds/_template/` to `lore/seeds/<your-seed-id>/`
250: 2. Edit `seed.json` (use the age-of-dragons-1024 seed as a template for the entity structure)
251: 3. Add lore markdown files in `factions/`, `characters/`, `regions/` subdirectories
252: 4. Run `PYTHONPATH=/path/to/ai-gm/src python -m pytest tests/ -v` — adjust tests so they pass locally before committing

253: The `seed_id` format: lowercase letters, digits, `-`, `_` only. No spaces, no non-ASCII characters, no dots.

254: ---

255: ## After install

256: - [README.md](README.md) — usage instructions, gameplay loop, roadmap
257: - [system_prompt.md](system_prompt.md) — the GM's behavior contract
258: - [schemas/README.md](schemas/README.md) — Option A schema mapping (rich → flat)
259: - [examples/turn-001-sample.jsonl](examples/turn-001-sample.jsonl) — sample first turn
260: - [tests/](tests/) — the plugin's integration suite
261: - The ai-gm core docs — `https://github.com/sigco3111/ai-gm`

262: ## License

263: Apache 2.0 — see [LICENSE](LICENSE).
