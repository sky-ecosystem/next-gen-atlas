---
id: 363b3afa-134c-4650-bd83-74e25152d5de
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `swapCurve`, which enforces `_checkRole(RELAYER)` before delegating the swap to `CurveLib.swap`.

`function swapCurve(
        address pool,
        uint256 inputIndex,
        uint256 outputIndex,
        uint256 amountIn,
        uint256 minAmountOut
    )
        external returns (uint256 amountOut)
    {
        _checkRole(RELAYER);`
