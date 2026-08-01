---
id: 10230cbb-8a2a-47c5-919c-93716d0ae170
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function unstakeSUSDe() external {
        _checkRole(RELAYER);`
