---
id: 4554fa6d-a03a-488d-a37e-a3be7b72323e
docNo: A.6.1.1.2.2.6.1.2.2.1.6.2
name: Tokenized Treasury Manager Admin Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.6.2 - Tokenized Treasury Manager Admin Role [Core]

The `MANAGER_ADMIN_ROLE` on a Tokenized Treasury Instance is authorized to configure rate providers, bounds for maximum swap size, oracle staleness, and fees, the Pocket contract, authorized redeemer contracts, and the fee claimer. The `MANAGER_ADMIN_ROLE` manages role assignments for the `MANAGER_ROLE`, `PAUSER_ROLE`, `REDEEMER_CONTRACT_ROLE`, and `REDEEMER_ROLE`. The `MANAGER_ADMIN_ROLE` is held by the Grove Proxy at `0x1369f7b2b38c76B6478c0f0E66D94923421891Ba` across all Tokenized Treasury Instances.
