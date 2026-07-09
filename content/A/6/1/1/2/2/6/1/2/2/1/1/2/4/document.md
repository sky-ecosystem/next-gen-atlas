---
id: abdc489a-6478-4e2a-9f22-423fd71d3700
docNo: A.6.1.1.2.2.6.1.2.2.1.1.2.4
name: Tokenized Treasury Pauser Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.2.4 - Tokenized Treasury Pauser Role [Core]

The `PAUSER_ROLE` on a Tokenized Treasury Instance is authorized to pause individual swap directions, credit token deposits and withdrawals, or all contract operations. Unpausing requires the `MANAGER_ADMIN_ROLE`. Additionally, the `PAUSER_ROLE` is authorized to revoke the `MANAGER_ROLE` and the `REDEEMER_ROLE` directly, bypassing the standard role-admin requirement. The `PAUSER_ROLE` is held by the [A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig](99bc2dd5-5573-4bb9-9210-5af299d058d9) across all Tokenized Treasury Instances.
