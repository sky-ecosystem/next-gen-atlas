---
id: 9a7a0d5e-ac6a-481d-ae61-d6504969524e
docNo: A.1.9.2.4.12.3.3.6
name: Spell Validators Should Review Oracle Address
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.6 - Spell Validators Should Review Oracle Address [Core]

Spell validators should ensure that oracle addresses are correctly verified.

To perform this validation the validators should go to the Chainlog and locate the relevant oracle (e.g. `PIP_ETH`). Take the contract address listed in the Chainlog to Etherscan. Open the "Read" tab of the contract on Etherscan. Look for the `src` value. Verify that the `src` value matches the `MedianETHUSDcontract` address referenced in the Spell.
