---
id: c646989c-15cc-4d74-892c-30f3593c8515
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.7
name: Decrease RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.7 - Decrease RateLimits [Core]

The operator must decrease the `LIMIT_UNISWAP_V3_DEPOSIT` rate limit for the `token0` and `pool` pair by `amount0`, and for the `token1` and `pool` pair by `amount1`, reflecting the tokens actually deposited.

`context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token0, address(pool)),
            amount0
        );
        context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token1, address(pool)),
            amount1
        );
    }`
