---
id: 616673d0-6961-495e-b8b0-335c0eedba25
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.5
name: Decrease Swap Rate Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.5 - Decrease Swap Rate Limit [Core]

The operator must decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by the value of the tokens being swapped in, before the exchange is executed.

`params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, params.pool),
            params.amountIn * rates[params.inputIndex] / 1e18
        );`
