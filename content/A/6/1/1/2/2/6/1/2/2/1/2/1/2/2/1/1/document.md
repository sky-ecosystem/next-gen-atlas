---
id: b2767d8e-f753-4dab-abd7-798dcd7b2311
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositERC4626`.

`function depositERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        returns (uint256 shares)`
