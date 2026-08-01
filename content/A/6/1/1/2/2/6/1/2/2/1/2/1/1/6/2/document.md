---
id: fac137fb-ba7f-474b-8406-77be9e9a3a25
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.2
name: Validate The Upper Tick Bound
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.2 - Validate The Upper Tick Bound [Core]

The operator must load the `uniswapV3PoolParams` for the `pool` and ensure the provided `upperTickBound` is greater than the pool's current `addLiquidityTickBounds.lower` and is less than or equal to the `MAX_TICK` of `887272`. Otherwise, the request reverts with `MainnetController/upper-tick-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        require(upperTickBound > params.addLiquidityTickBounds.lower && upperTickBound <= MAX_TICK, "MainnetController/upper-tick-out-of-bounds");`
