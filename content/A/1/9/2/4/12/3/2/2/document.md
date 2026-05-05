---
id: 83f53a73-7e2f-4dc9-a371-e19238924bf3
docNo: A.1.9.2.4.12.3.2.2
name: Spell Validators Must Check Compiler Version
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.2.2 - Spell Validators Must Check Compiler Version [Core]

Validators should ensure that the Solidity compiler version used in the deployed Spell matches the version specified in the `Spells-mainnet` repository on GitHub. Validators should verify this by:

- Navigate to the "Contract" tab on Etherscan and check the `Compiler Version` field under the contract’s metadata. The version displayed must match the version specified in the `DssSpell.sol` contract (e.g., pragma solidity `0.8.16`;).
- Only the first part of the version (e.g., `v0.8.16`) needs to match; any additional commit information can be ignored.

While the Spell should use the correct version to pass validation, this is not considered a strict requirement.
