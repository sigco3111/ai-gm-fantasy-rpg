## [CHUNK: rule -- NPC Reactions]
# triggers: npc, reaction, disposition
# priority: 6

On first meaningful contact, assign an NPC disposition: hostile, unfriendly, indifferent, friendly, or helpful. Treat disposition as a single tag that gates social options and mechanical responses; hostile NPCs will refuse service and may call guards, helpful NPCs offer aid, information, or discounts.

Disposition is recorded simply (tag or small integer) and applies to the scene. Actions move disposition in deterministic steps: overt aggression or theft moves two steps toward hostile; clear aid or gifts move one step toward helpful. A successful Persuasion/Deception/Intimidation roll may move disposition one step toward the player's intent.

When disposition changes, the GM announces one immediate mechanical consequence (price adjustment, refusal, offered information, alerting authorities). Apply shifts conservatively: avoid multiple compounded penalties for a single minor action. For group interactions, use the party's leading actor or a representative social roll to determine a single shift.

Guidance: disposition gates available interaction trees, it is not a substitute for roleplay. Use it to resolve access, prices, and simple behaviors quickly so the narrative can continue.

## [CHUNK: rule -- Persuasion, Deception, Intimidation]
# triggers: persuasion, deception, intimidation
# priority: 7

Resolution: opposed check, player d20 + CHA modifier versus NPC d20 + Insight modifier. Declare Persuasion, Deception, or Intimidation before rolling. NPC Insight is a static modifier based on NPC role and perception (+0 commoners, +4 experienced, +6+ for specialists).

Mechanics: a success grants the stated short-term effect (belief, compliance, better price) and typically shifts disposition one step toward the player's intent. Failure grants no benefit and may shift disposition against the player. Natural 20 is a critical success: apply effect and an extra favorable shift. Natural 1 is a critical failure: double the adverse shift and risk immediate hostility.

Degrees of success: marginal (win by 1-4) grants a small concession; clear (5-9) a meaningful result; decisive (10+) a full or extended concession. Use these bands to scale effects (minor price reduction, free information, temporary assistance).

Modifiers and situational factors: apply situational modifiers (+/-2 to +/-6) for leverage, prior reputation, presented evidence, or social terrain (a trial hall vs a dive tavern). Announce modifiers prior to the roll and record them when they matter.

Teamwork: allies may assist with Aid actions to grant advantage or a flat bonus; the GM adjudicates when multiple speakers alter the contest.

## [CHUNK: rule -- Reputation and Renown]
# triggers: reputation, renown, faction
# priority: 5

Track reputation by faction on a -100 to +100 scale. Discrete acts map to reputation deltas: small help +5, notable aid +15, betrayal -20, major crimes -50. Local renown is tracked separately per settlement and affects public standing and local benefits.

Thresholds and effects: faction reputation >= +40 grants institutional favors or access; <= -40 results in rejection, sanctions, or bounties. Local renown >= +40 grants "hero" benefits (discounts, invitations, assistance); <= -40 grants "villain" consequences (refusals, bounties). Faction reputation can mitigate local penalties for faction allies.

Administration: record reputation events with date, location, and magnitude. Reputation decays slowly (1-2 points per month without interaction). Repairing reputation requires deliberate actions: quests, reparations, or expenditures. Reputation is independent per faction; do not conflate scores.

Narrative note: reputation changes should be visible when they produce mechanical effects, but provenance may stay hidden until discovered by players via inquiry checks.

## [CHUNK: rule -- Trade and Haggling]
# triggers: trade, haggle, merchant
# priority: 6

Merchants post base prices and maintain buy/sell margins. Haggling resolves as opposed roll: buyer d20 + CHA modifier vs merchant d20 + Trade Skill modifier. Merchant Trade Skill indicates experience and sets buy/sell margins: unskilled merchants buy at 50-60% of base, skilled merchants at 70-85%.

Discount table by degree: marginal success (win by 1-4) yields 1d4% off; clear (5-9) yields 5-8%; decisive (10+) yields 9-12% off base. Failure increases price by 5% and may end the negotiation.

Criticals: natural 20 grants an additional 5% discount and a +1 disposition shift toward the buyer. Natural 1 imposes a 10% penalty and may cause refusal to trade.

Practical rules: include a local market modifier (+/- % for supply/demand). Resolve with a single opposed roll per negotiation unless the player spends time to press the matter. Repeated failed haggles incur merchant annoyance; after three failed attempts a merchant refuses further haggling for 24 hours.

When players sell goods, roll merchant Trade Skill secretly to set an offer within the merchant's buy margin. Allow players with Trade contacts or relevant skills to reduce margins or gain pre-negotiation knowledge.

## [CHUNK: rule -- Rumors and Information]
# triggers: rumor, tavern, gossip
# priority: 5

A visit to a public hub yields 1d4 rumor topics. Default distribution: 1 true, 2 possible, 1 false. Tag each rumor as true, possible, or false; GMs may seed plot hooks or red herrings among them.

Verification: players may spend time/resources to investigate. Resolution is d20 + Investigation modifier against a static TN based on the tag: true TN 10, possible TN 13, false TN 16. Success upgrades reliability, reveals provenance, or supplies actionable leads. Failure may confirm a falsehood or waste resources.

Use a short rumor log to track sources, tags, and whether players have investigated them. Encourage cross-checking: corroboration from multiple independent sources lowers TNs for verification. Rumors point to leads, not automatic solutions; follow-up investigation yields concrete mechanical outcomes.

GM guidance: keep rumors concise, avoid contradictions, and ensure they serve scene pacing. Record essential rumor provenance when it ties to plot-critical events.
