---
id: a109ad0d-0743-4ae9-bcc1-df04a6e5da43
docNo: A.1.9.2.3.2.3.2.1
name: Sky Core Spell Executes Agent Spell
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.3.2.3.2.1 - Sky Core Spell Executes Agent Spell [Core]

Execution of an Agent Spell is initiated by the Sky Core Spell, which directly calls `exec()` on the Agent's SubProxy contract to perform the Spell’s actions in the same transaction. The SubProxy limits rights to the specific Agent, preventing access to Sky Core contracts. The current SubProxy contract is designed to execute the Agent Spell in the same transaction as the Sky Core Spell.
