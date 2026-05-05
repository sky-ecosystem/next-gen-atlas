---
id: 97f4831e-1566-46e1-bbac-2a668e4b5ca7
docNo: A.1.9.2.4.12.3.3.3
name: Spell Validators Should Review Spell Actions
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.3 - Spell Validators Should Review Spell Actions [Core]

Validators should ensure that all values before and after the Spell actions are constants or immutable. If values are not constants, they could present malicious code in the form of memory mutations impacting the function of the pause proxy.

To perform this validation, the validator must go to the "Contract" tab on Etherscan and review the source code.
