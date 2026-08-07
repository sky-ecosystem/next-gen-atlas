---
id: 61690505-13a7-4b3d-ad1d-a27802e0c69a
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimDepositERC7540`.

`function claimDepositERC7540(address token) external {
        _checkRole(RELAYER);`
