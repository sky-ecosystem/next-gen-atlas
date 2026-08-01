---
id: ef00ff33-d1a0-49c0-bf6c-50f8e8b83706
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositAave`, which is enforced by the `_checkRole` check at the start of the function.

`function depositAave(address aToken, uint256 amount) external {
        _checkRole(RELAYER);`
