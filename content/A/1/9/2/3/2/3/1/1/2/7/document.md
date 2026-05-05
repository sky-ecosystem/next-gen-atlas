---
id: 8113159f-dcf6-4c44-afb0-aed09b1e5cf7
docNo: A.1.9.2.3.2.3.1.1.2.7
name: Function Call For Execution
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.1.9.2.3.2.3.1.1.2.7 - Function Call For Execution [Core]

Execution is initiated on the StarGuard contract via its `exec()` function, which performs necessary validation checks before calling the SubProxy’s `exec(spellDataCopy.addr, abi.encodePacked(StarSpellLike.execute.selector))` to perform the Spell's actions.
