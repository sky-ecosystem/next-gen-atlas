---
id: 0b72eee2-1068-4d6a-8a47-f342d7672c89
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeMint`, which is enforced by the `_checkRole` check at the start of the function.

`function prepareUSDeMint(uint256 usdcAmount) external {
        _checkRole(RELAYER);`
