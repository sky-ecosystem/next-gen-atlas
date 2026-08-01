---
id: a4ee29f7-f12f-4da4-89eb-997c7dc30c35
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeBurn`, which is enforced by the `_checkRole` check at the start of the function.

`function prepareUSDeBurn(uint256 usdeAmount) external {
        _checkRole(RELAYER);`
