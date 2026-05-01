---
id: d6e0c32d-aea2-4bc7-9ec3-97d54bdbd9a7
docNo: A.3.7.1.1.2.6
name: Debt Floor (dust)
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.7.1.1.2.6 - Debt Floor (dust) [Core]

The Debt Floor parameter controls the minimum amount of Dai that can be minted using a specific vault type for an individual vault. If a user tries to mint Dai and the amount of Dai minted would not put the vault's amount of Dai minted above its Debt Floor, the transaction will fail and no DAi will be minted. Likewise, if a user attempts to pay back debt such that their debt will equal less than the Debt Floor and greater than zero, the transaction will fail and no Dai will be paid back. Each vault type has its own Debt Floor that can be adjusted by Sky Governance.
