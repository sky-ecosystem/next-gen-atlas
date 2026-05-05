---
id: 4674dbfa-77d8-4d99-980e-330342b0ffa9
docNo: A.1.9.2.4.12.3.3.13
name: Spell Validators Should Check For Hidden Or Unverified Contracts
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.13 - Spell Validators Should Check For Hidden Or Unverified Contracts [Core]

Validators should check for hidden or unverified contracts linked to the Spell (e.g., libraries or proxies).

To perform these checks, the validator must go to the "Contract" tab on Etherscan and review the source code. Scan the code for any referenced contracts or addresses: Look for imports, inherited contracts, hardcoded addresses, or function calls to external contracts. If it's an address, search it directly on Etherscan and confirm it's verified (e.g., green checkmark with available source code). Compare the referenced code to the official GitHub repository (e.g., Spells-mainnet repo) to ensure versions match and nothing has been altered.
