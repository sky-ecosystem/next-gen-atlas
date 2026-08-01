---
id: f4095845-57ef-4e67-9260-c0dfe347c5a5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimCentrifugeCancelDepositRequest`.

`function claimCentrifugeCancelDepositRequest(address token) external {
        _checkRole(RELAYER);`
