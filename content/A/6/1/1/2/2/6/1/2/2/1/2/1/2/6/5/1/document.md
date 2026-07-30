---
id: 00b5dd72-7013-4fd5-8ad8-e00f0935cd19
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferSharesCentrifuge`. The function is `payable` so the operator can forward the cross-chain messaging fee.

`function transferSharesCentrifuge(
        address token,
        uint128 amount,
        uint16  destinationCentrifugeId
    )
        external payable
    {
        _checkRole(RELAYER);`
