---
id: 0c80de53-a7d0-45c1-9b5a-9efccb990b77
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimRedeemERC7540`.

`function claimRedeemERC7540(address token) external {
        _checkRole(RELAYER);`
