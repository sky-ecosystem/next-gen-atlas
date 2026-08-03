---
id: 75c217fb-18f8-458b-a933-5c57b4abeeaa
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawERC4626`.

`function withdrawERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        returns (uint256 shares)`
