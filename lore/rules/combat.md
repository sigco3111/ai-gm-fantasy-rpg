## [CHUNK: rule -- Melee & Ranged Combat]
# triggers: melee, ranged, attack
# priority: 6

Core attack resolution uses a single d20 roll plus the attacker's relevant modifier.
Roll d20 + modifier against the defender's AC. If the total meets or exceeds AC, the attack hits.

Damage is calculated as the weapon or effect value; final HP loss equals the damage value.
For contested strikes (both parties hit simultaneously) the net effect on tactical HP may be treated by the GM as damage equal to each individual damage result; do not subtract defenses twice.

Hit points are tracked per-character as discrete points. One point of damage reduces HP by one.
Treat creature HP as an abstract pool; fractional effects round down unless explicitly stated.

When using ranged attacks, apply the usual d20 attack roll, then check range bands for penalties.
Long range imposes disadvantage on the attack roll; cover grants +2 AC to the defender unless otherwise noted.

Summary: attack = d20 + modifier vs AC. Damage equals the weapon's damage entry. HP is reduced point-for-point.

## [CHUNK: rule -- Magic in Combat]
# triggers: magic, spellcasting, concentration
# priority: 7

Casting a spell in the heat of battle generally consumes a spellcaster's full action unless the spell states otherwise.
The caster rolls d20 + spellcasting modifier for any attack roll required by the spell; defensive saves follow normal save mechanics.

Concentration: certain spells require concentration to maintain. If a caster takes damage while concentrating, they must succeed on a CON save (DC = 10 or half the damage taken, whichever is higher) to maintain concentration.
Failure drops the spell immediately; the effect ends and may be interrupted by subsequent actions.

Interrupt mechanics: a reaction or readied action can interrupt a spell that has a verbal or somatic component if the interrupting action succeeds before the spell's completion.
Area spells and instantaneous effects resolve on cast; concentration-dependent ongoing effects are vulnerable to disruption by failed saves.

Quick-casting items or rituals require explicit GM approval and typically forfeit the right to make attacks of opportunity during the same turn.

## [CHUNK: rule -- Dragon Encounters]
# triggers: dragon, breath, fear
# priority: 9

Dragons are treated as apex creatures with layered defenses. They have damage resistances based on age and type; apply resistance before HP reduction.
If a dragon resists an element, halve incoming damage of that element (round down) unless a specific bypass is used.

Breath Weapon: a dragon's breath is a recharge action (see creature stat block); it is resolved as a cone or line template. Targets in the template make the indicated save or take full breath damage; successful saves take half.
Breath weapons ignore half cover but do not negate total cover unless explicitly stated.

Fear Aura: adult and older dragons emanate a fear aura. Entering or starting a turn in the aura forces a Wisdom save (DC per dragon) or the creature becomes frightened for one round.
Any creature reduced to 0 HP while frightened must make a morale check (see Morale and Rallying) before dying or routing.

Tactics: dragons use flight and terrain to maximize breath and minimize enemy adjacent attacks. Mounted or massed forces should use focused ranged volleys and anti-drake ordnance.

## [CHUNK: rule -- Morale and Rallying]
# triggers: morale, panic, rally
# priority: 6

The GM sets the triggering condition; individual morale checks use d20 + leadership or morale modifier versus a difficulty determined by the situation.

On a failed morale check, a unit may break and retreat, becoming unavailable for actions until rallied.
A successful rally requires a leadership action: a leader within visible range may spend an action to attempt a rally roll (d20 + leader modifier vs DC). Success restores cohesion and allows normal actions next round.

Units that route suffer a -2 penalty to future morale checks until they complete a full rest or are explicitly rallied by a competent leader.
Massed creatures (swarms, militia) treat morale at group level; individual PCs may be required to make independent checks when the group breaks.

## [CHUNK: rule -- Death and Resurrection]
# triggers: death, revive, soul
# priority: 8

Death saves: when reduced to 0 HP, a character begins making death saving throws at the start of each turn: roll d20—10 or higher is a success, below 10 is a failure.
Three successes stabilize the character; three failures cause true death. Any damage while at 0 HP counts as an automatic failure and may increase the death tally.

Revivify-style magic: spells named for resurrection require a successful ritual or spell (GM confirms components). Most such spells return a soul if cast within a specified window (commonly minutes to days depending on spell tier).
Revivify attempts restore a fraction of HP on success and may carry side effects (memory loss, temporary frailty) at the GM's discretion.

Soul-binding and true death: permanent death happens when a soul is destroyed or irretrievably bound. Soul-binding requires a complex ritual, costly components, and leaves the target altered.
By default, true death prevents resurrection without a high-tier intervention (arch-mage, artifact, or deity). The GM must record any soul-binding acts and the conditions required to reverse them.
