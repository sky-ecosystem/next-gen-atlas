---
id: 3bf9b752-398b-4c53-8a32-608619621193
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUniswapV3`. The function exchanges `tokenIn` for the pool's other token through the Uniswap V3 `router`.

`function swapUniswapV3(
        address pool,
        address tokenIn,
        uint256 amountIn,
        uint256 minAmountOut,
        uint24  swapMaxTickDelta
    )
        external returns (uint256 amountOut)
    {
        _checkRole(RELAYER);`
