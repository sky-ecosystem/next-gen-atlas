---
id: b2a472a5-d4c5-4504-ae75-842f8fb90a01
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimCentrifugeCancelRedeemRequest`.

`function claimCentrifugeCancelRedeemRequest(address token) external {
        _checkRole(RELAYER);`
