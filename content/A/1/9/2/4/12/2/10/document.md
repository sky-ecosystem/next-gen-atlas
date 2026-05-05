---
id: 230c15db-6c5a-4486-b44b-ef915db39d11
docNo: A.1.9.2.4.12.2.10
name: Using Etherscan Website For Spell Validation
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.2.10 - Using Etherscan Website For Spell Validation [Core]

The use of the Etherscan website is required when validating Spells, as it is the only blockchain explorer that displays the verified code of the current Spell’s smart contract, including its Solidity compiler version, licensing settings, optimization settings, and libraries used.

Aside from the current Spell’s smart contract, using Etherscan to make calls to, interact with, or read information from other smart contracts is not required during the validation process. Many smart contracts associated with the Sky Protocol have only been verified on Etherscan.

Automated Spell deployment and code comparison scripts within the Spell repositories may require an Etherscan API key; however, these scripts must not be used when validating Spells.
