---
id: d96cfa41-45bd-43c1-a0b8-22d6ec624104
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.2
name: Validate Position Parameters
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.2 - Validate Position Parameters [Core]

The operator must validate the removal parameters, ensuring the position's tokens and fee match the `pool` and that the requested `liquidity` is greater than zero and does not exceed the position's liquidity.

`function removeLiquidity(UniV3Context calldata context, RemoveLiquidityParams calldata params)
        external
        returns (uint256 amount0Collected, uint256 amount1Collected)
    {
        IUniswapV3PoolLike pool = IUniswapV3PoolLike(context.pool);

        (address token0, address token1) = _validateRemoveLiquidityParams(pool, params);`
