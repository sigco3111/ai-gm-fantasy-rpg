## [CHUNK: rule -- Wilderness Travel]
# triggers: travel, forage, encounter
# priority: 6

Wilderness travel sets the rhythm of the campaign between hearth and high road. Choose a pace: slow (1/2 movement, +2 to forage checks, -2 to random encounter chance), normal (standard movement, no modifiers), or fast (+50% movement, -2 to forage checks, +2 to encounter chance). Forage checks are d20 + Survival or Wisdom modifier; on a natural 20 treat the result as exceptional forage: 2d4 rations or useful herb finds.

Random encounters are resolved with a 1d20 roll against the regional encounter table supplied by the GM. Roll once per travel segment (every 4 hours of travel at normal pace, every 2 hours at fast pace, every 6 at slow pace). A successful Stealth or Perception contest may alter or avoid the encounter.

## [CHUNK: rule -- Dungeon Delving]
# triggers: dungeon, torch, mapping
# priority: 7

Dungeon delving specifies light, mapping, and rest rules. Light sources: torch burns ~1 hour, lantern burns ~4 hours, magical light per item description, darkvision provides effective vision without consuming light. Track remaining burn time; when light expires, characters without darkvision suffer normal darkness penalties.

Mapping is encouraged: each 5 minutes spent mapping an adjacent square reveals feature and hazards; a competent mapper (Proficiency with cartography tools or Investigation check) reduces mistakes. Rest cycles underground follow standard rest rules, but long rests require a secure chamber or watch allocation.

## [CHUNK: rule -- Rest Cycles]
# triggers: rest, short rest, long rest
# priority: 5

Short rests last 1 hour. During a short rest a character may spend hit dice to regain HP; when a short rest completes, roll 1d8 per hit die spent plus Con modifier per die. Long rests last 8 hours, restore full HP and half of spent hit dice (minimum 1), and reset most class abilities. A long rest in hostile terrain requires a successful group Survival check or an established camp, otherwise count as interrupted.

Interruptions: any encounter, environmental hazard, or failed watch check that causes combat or immediate danger interrupts a rest. If interrupted during a long rest, resolve whether the group can return to rest within 1 hour; failure converts the long rest into a short rest (no full HP recovery, only hit dice regained as per short rest rules).

## [CHUNK: rule -- Perception and Traps]
# triggers: perception, trap, detect
# priority: 6

Perception uses passive and active measures. Passive Perception equals 10 + Perception modifier; the GM may use passive values to determine if wandering traps or ambushes are noticed. Active trap detection is a d20 + Investigation or Perception check against a trap's detection DC. A roll equal to or greater than the DC reveals the trap's presence and general nature.

Trap disarming requires thieves' tools plus a Dexterity check (d20 + DEX modifier + proficiency if proficient with thieves' tools) against the trap's disarm DC. Failure may trigger the trap; on a natural 1 the trap triggers automatically. The GM adjudicates partial successes (disarm with complications) with a minimal scripted consequence.

## [CHUNK: rule -- Weather and Hazards]
# triggers: weather, hazard, environment
# priority: 5

Weather and hazards impose environmental checks and potential damage. Extreme cold causes exposure checks: a failed Constitution saving throw (DC determined by region and severity) deals 1d6 cold damage per hour and exhaustion. Swamps may force Disease checks: on failure the character contracts a minor illness that imposes -1 to STR/DEX for 24 hours unless treated.

Region-specific hazards: mountain ranges impose thin-air checks for climbing and grant a risk of rockfall (1d6 bludgeoning on failed Dexterity save), coastal/drake territories require an Awareness roll to avoid wyvern/drake patrols, swamp territories have hidden sinkholes (Dex save to avoid falling). The GM should provide a simple table per region mapping d20 ranges to hazard events.
