---
id: b5bbbdfc-362f-4e71-a09d-2b52e200afb7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `requestDepositERC7540`.

`function requestDepositERC7540(address token, uint256 amount) external {
        _checkRole(RELAYER);`
