---
id: 438343b7-8d2a-4698-8d0f-2ab01a570ff8
docNo: A.1.9.2.4.12.3.1.4
name: Spell Validators Must Check Deployed Spell Code
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.4 - Spell Validators Must Check Deployed Spell Code [Core]

The Spell validator must ensure that the deployed Spell code matches the Spell code present in the GitHub Repository.

In order to pass validation, the deployed Spell must not contain any potentially malicious code or any notable functional changes within the `DssSpellAction`.

The validation for the Spell code can be done by using the `diff-deployed-Spell` script present in the Spell repository on GitHub to ensure that the deployed Spell’s code matches locally compiled code. Alternatively, an online tool like diff checker ([https://www.diffchecker.com/](https://www.diffchecker.com/)) can be used. The Spell code on Etherscan should be compared with the `DssSpell.sol` in the GitHub repository for the relevant Spell. If the Spell goes live before the code is merged to the main branch, it’s possible to find the branch by the Target Date name of the Spell (e.g., YYYY-MM-DD).

When comparing, note that the following differences are acceptable and should not be flagged (based on validation guides):

- Comments: Lines starting with `//` or inside `/* */`.
- Imports and Solidity versions: Multiple declarations in the GitHub code.
- Interfaces: Numerical suffixes like `_1` or `_2` added to interface names in the contract.
- DssExecLib Interface: Extra code or warnings within the `DssExecLib` library.
