---
id: a1773da6-7656-47b7-a31a-a4bd366d0d85
docNo: A.1.9.2.4.12.3.1.8
name: Spell Validators Must Check Deployed Spell EVM Version
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.8 - Spell Validators Must Check Deployed Spell EVM Version [Core]

Validators must ensure that the correct EVM version for the Spell contract is displayed on Etherscan. The EVM version is determined by the Solidity compiler version used during compilation. For the Spell to pass validation, the `Other Settings` field on Etherscan must display either "Default" or the correct default EVM version name for that compiler release (e.g., for Solidity 0.8.16, either "Default" or "London" is acceptable, as London is the default EVM for that compiler version).

To perform this validation, the validator must go to the "Contract" tab on Etherscan and review the `Other Settings` field under the contract’s metadata.
