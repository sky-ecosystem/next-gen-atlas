---
id: cdd724f1-5cc7-48df-81f7-25c6a932a184
docNo: A.1.9.2.4.13.4.1
name: Casting Of Spell
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.13.4.1 - Casting Of Spell [Core]

When the `cast` function in the DssSpell contract is called:

- The Spell is marked as `cast`, preventing it from being executed again.
- The `cast` function initiates the execution process by calling the `exec` function in the `ds-pause` contract.
