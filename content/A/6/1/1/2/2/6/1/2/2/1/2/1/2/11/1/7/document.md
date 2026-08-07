---
id: 8bfd464e-eb67-48bf-8a83-ae10fecb783d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.7
name: Decrease RateLimit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.7 - Decrease RateLimit [Core]

The operator must decrease the rate limit after the redemption by the amount of `tokenOut` received, using a key derived from `LIMIT_PENDLE_PT_REDEEM` and the `pendleMarket` address. Note that `redeemPendlePT` must not be used for markets with non-standard SYs (such as ePENDLE, mPENDLE, or aTokens like aUSDC and aUSDT) without additional testing targeting each such market.

`        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, address(params.pendleMarket)),
            totalTokenOutAmount
        );

    }`
