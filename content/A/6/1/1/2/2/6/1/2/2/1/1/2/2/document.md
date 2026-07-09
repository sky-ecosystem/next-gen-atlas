---
id: 4554fa6d-a03a-488d-a37e-a3be7b72323e
docNo: A.6.1.1.2.2.6.1.2.2.1.1.2.2
name: Tokenized Treasury Manager Admin Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.2.2 - Tokenized Treasury Manager Admin Role [Core]

The `MANAGER_ADMIN_ROLE` on a Tokenized Treasury Instance is authorized to configure rate providers, bounds for maximum swap size, oracle staleness, and fees, the Pocket contract, authorized redeemer contracts, and the fee claimer. The `MANAGER_ADMIN_ROLE` manages role assignments for the `MANAGER_ROLE`, `PAUSER_ROLE`, `REDEEMER_CONTRACT_ROLE`, and `REDEEMER_ROLE`. The `MANAGER_ADMIN_ROLE` is held by the Grove [A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account](d143241d-5819-432d-a6ba-892961502838) across all Tokenized Treasury Instances.
