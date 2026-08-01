---
id: 01fe4914-7846-43ff-820b-52a70bf6ef17
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cancelCentrifugeRedeemRequest`.

`function cancelCentrifugeRedeemRequest(address token) external {
        _checkRole(RELAYER);`
