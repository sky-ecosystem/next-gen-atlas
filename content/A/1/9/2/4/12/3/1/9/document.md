---
id: 46cbc700-20e4-4a57-9508-07a6baa26fca
docNo: A.1.9.2.4.12.3.1.9
name: Spell Validators Must Perform Basic Spell Code Validation
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.9 - Spell Validators Must Perform Basic Spell Code Validation [Core]

The Spell validator must perform a brief review of the Spell code. This includes reviewing the `DssSpellAction` contract within the `DssSpell.sol` file.

Validators should look for any unusual behavior, such as:

- Low-level assembly operations (e.g., `assembly` blocks).
- The use of Solidity opcodes, such as `delegatecall`, `callcode`, or `selfdestruct`.
- Suspicious-looking payments or transfers.
- Any other malicious or unauthorized code. This includes cross-checking the Solidity code in `actions()` against the Executive Sheet and the Executive Document. Each action must be authorized per the Atlas.

Spell validators must report any code they find that appears to be malicious or which likely forms part of an attempted attack. A Spell must not pass validation if the Spell validator is convinced that malicious code is present in a Spell or that its execution can lead to an attack on the Sky Protocol.

To perform this validation, the validator must go to the "Contract" tab on Etherscan and review the source code.
