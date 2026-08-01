---
id: ec105dad-7ddc-4973-b3f5-c1cb92667a5b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownAssetsSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function cooldownAssetsSUSDe(uint256 usdeAmount) external {
        _checkRole(RELAYER);`
