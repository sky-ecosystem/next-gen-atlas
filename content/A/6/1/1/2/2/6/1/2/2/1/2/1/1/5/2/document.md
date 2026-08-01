---
id: 020bdec4-2ffb-4ad7-aa21-38d290405cfa
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.2
name: Validate The Lower Tick Bound
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.2 - Validate The Lower Tick Bound [Core]

The operator must retrieve the stored `UniswapV3PoolParams` for the `pool` and ensure the supplied `lowerTickBound` is greater than or equal to `MIN_TICK` (-887272) and strictly less than the pool's current upper `addLiquidityTickBounds`. Otherwise the call reverts with `MainnetController/lower-tick-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        require(lowerTickBound >= MIN_TICK && lowerTickBound < params.addLiquidityTickBounds.upper, "MainnetController/lower-tick-out-of-bounds");`
