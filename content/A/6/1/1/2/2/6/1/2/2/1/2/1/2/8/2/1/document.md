---
id: de2ec5fb-8fbb-48e0-8f57-d53cc0d0eee3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `addLiquidityCurve`, which enforces `_checkRole(RELAYER)` before delegating the deposit to `CurveLib.addLiquidity`.

`function addLiquidityCurve(
        address pool,
        uint256[] memory depositAmounts,
        uint256 minLpAmount
    )
        external returns (uint256 shares)
    {
        _checkRole(RELAYER);`
