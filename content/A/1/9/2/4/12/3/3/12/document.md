---
id: fdcea934-c3fb-4735-acc3-3e320ad89b00
docNo: A.1.9.2.4.12.3.3.12
name: Spell Validators Should Verify The Contract ABI
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.12 - Spell Validators Should Verify The Contract ABI [Core]

Validators should verify that the contract ABI (Application Binary Interface) is correctly generated and matches the deployed contract.

To perform this check, the validator must go to the "Contract" tab on Etherscan and the "Contract ABI" section. Copy the ABI JSON and compare it against the expected ABI from the official GitHub repository (e.g., Spells-mainnet repo). To obtain the expected ABI from the GitHub repository download the relevant Solidity file, paste it into a tool like Remix IDE, select the matching compiler version, and compile to extract the ABI JSON. Use a diff tool to check for exact matches in functions, parameters, and types.
