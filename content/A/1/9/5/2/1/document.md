---
id: 022b27ab-220d-4411-bfc8-5d09681ecc48
docNo: A.1.9.5.2.1
name: Standby Spells Definition
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.5.2.1 - Standby Spells Definition [Core]

Sky Protocol uses circuit-breakers to mitigate undesired scenarios, which circuit-breakers are called MOM contracts. MOM contracts must first be triggered through a spell, after which they bypass the GSM Pause Delay and can immediately act on the Protocol. See [A.1.9.3.2 - Exceptions](6781594b-5dff-45ec-89a4-1c9684c4eed8).

In emergency scenarios, time is a scarce resource. Therefore, Standby Spells are used in validated emergency scenarios to trigger a MOM contract. In an emergency situation, spell teams can then focus on crafting an ad hoc Emergency Spell to solve the root cause of an issue, if appropriate. Due to Standby Spells, it is no longer necessary in an emergency for spell teams to spend time crafting and reviewing a spell whose sole purpose is to trigger a mitigation of the issue, i.e., the MOM contract.

Standby Spells open new attack vectors that must be mitigated pursuant to [A.1.9.5.2.3.3 - ADs' Role In Standby Spells](53cea69b-45cc-4f9c-b863-9bf259e37deb).
