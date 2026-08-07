---
id: b83bc58c-f6b0-45a1-9ff8-4e705f8f5476
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.2
name: Check Max Tick Delta Bounds
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.2 - Check Max Tick Delta Bounds [Core]

The operator must ensure the `maxTickDelta` is greater than `0` and does not exceed `UniswapV3Lib.MAX_TICK_DELTA` (`887272`), otherwise the call reverts with `max-tick-delta-out-of-bounds`.

`        require(
            maxTickDelta > 0 &&
            maxTickDelta <= UniswapV3Lib.MAX_TICK_DELTA,
            "MainnetController/max-tick-delta-out-of-bounds"
        );`
