---
id: 9ce4d08e-aa5b-4cab-884e-7a53e937bdb8
docNo: A.3.7.1.1.2.1
name: Liquidation Ratio
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.7.1.1.2.1 - Liquidation Ratio [Core]

The Liquidation Ratio parameter limits the maximum amount of Dai debt that a vault user can draw from their vault given the value of their collateral locked in that vault. In practice, it expresses the minimum collateral in percentage terms that can support a given Dai debt. If the ratio of a Vault user's collateral to their debt drops below this value, their vault can be liquidated. Each vault type has its own Liquidation Ratio. The Liquidation Ratio for each vault type is expressed as a percentage value of the collateral that must be present in the vault to support its debt.

Changes to the Liquidation Ratio are subject to the Operational Weekly Cycle, requiring a Governance Poll followed by an Executive Vote.
