---
id: 6646540e-4b82-4cc0-bcbc-b733648be9ea
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.3
name: Set The Pool Max Tick Delta
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.3 - Set The Pool Max Tick Delta [Core]

The operator must set the `swapMaxTickDelta` on the `uniswapV3PoolParams` for the given `pool` to the supplied `maxTickDelta`.

`        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        params.swapMaxTickDelta = maxTickDelta;`
