---
id: fbd75855-2a62-4572-bb63-f0907343f033
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `toggleOperatorMerkl`.

`function toggleOperatorMerkl(address operator) external {
        _checkRole(RELAYER);`
