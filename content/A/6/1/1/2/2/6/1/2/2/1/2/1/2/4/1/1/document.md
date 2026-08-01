---
id: 2ff99ee2-a0ce-4280-a9e3-5aa0042e5cd5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferAsset`.

`function transferAsset(address asset, address destination, uint256 amount) external {
        _checkRole(RELAYER);`
