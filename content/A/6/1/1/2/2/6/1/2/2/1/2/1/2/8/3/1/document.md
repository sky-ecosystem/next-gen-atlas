---
id: 66cab13d-bdbf-4116-9be6-204e136f6829
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `removeLiquidityCurve`, which enforces `_checkRole(RELAYER)` before delegating the withdrawal to `CurveLib.removeLiquidity`.

`function removeLiquidityCurve(
        address   pool,
        uint256   lpBurnAmount,
        uint256[] memory minWithdrawAmounts
    )
        external returns (uint256[] memory withdrawnTokens)
    {
        _checkRole(RELAYER);`
