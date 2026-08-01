---
id: d2558ce3-2378-4794-938f-81dae9846231
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `addLiquidityUniswapV3`. The function mints or increases a liquidity position in the given Uniswap V3 `pool`.

`function addLiquidityUniswapV3(
        address                   pool,
        uint256                   tokenId,
        UniswapV3Lib.Tick         calldata tick,
        UniswapV3Lib.TokenAmounts calldata target,
        UniswapV3Lib.TokenAmounts calldata min,
        uint256                   deadline
    )
        external
        returns (uint256 tokenId_, uint128 liquidity_, uint256 amount0_, uint256 amount1_)
    {
        _checkRole(RELAYER);`
