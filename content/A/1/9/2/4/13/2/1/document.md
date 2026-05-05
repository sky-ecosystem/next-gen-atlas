---
id: f31bd0d0-fc5b-4c86-9b84-30c4b010c986
docNo: A.1.9.2.4.13.2.1
name: Chief-keeper
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.13.2.1 - Chief-keeper [Core]

The chief-keeper monitors and interacts with DSChief and DSSSpells. When a Spell receives more approval than the current hat, the chief-keeper calls the `lift` function to make this Spell the new hat. After confirming hat status, the chief-keeper proceeds to schedule the Spell, ensuring that only the current hat is scheduled for execution.
