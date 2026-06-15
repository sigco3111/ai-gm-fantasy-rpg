# Schemas — ai-gm-fantasy-rpg

This plugin does NOT define its own JSON schemas. It reuses the canonical schemas from the ai-gm core.

Reference path from this plugin root:

../ai-gm/schemas/

Required schema files

The plugin's seed.json MUST conform to the following core schemas. Each file below is maintained in the ai-gm core repository.

- state.json — top-level state shape, including fields such as game_id, schema_version, turn, created_at, event_log, entities
- event.json — event payload shape used by advance_turn, including event_id, turn, actor_id, action, payload, reason
- entity.json — entity shape used for all game entities, including id, type, name, attributes
- lore_chunk.json — chunk shape produced by the markdown chunker, including type, name, content, triggers, priority

Notes and conventions

- If you need to add a new entity type or attribute, the schema MUST be updated in the core ai-gm repo, not here. This plugin only references core schemas to stay compatible with other plugins and tools.

- The fantasy-rpg seed uses three entity types defined in the core schema: faction, character, province. Party members are character entities with a party_id attribute.

- Spells, quests, and items are treated as GM-narrative concepts and are not modeled as persistent state entities in this plugin. They belong in lore markdown only, and can be surfaced via lore_chunk.json entries.

Where to look in the core repo

See ../ai-gm/schemas/ for the authoritative schema files and any updates. When in doubt, align seed.json with the latest core schema versions before publishing.

Contact

If you need schema changes, open a pull request against the ai-gm core repository and reference this plugin's seed use cases.
