---
id: afb2942a-2f4c-4201-8d46-eca71f2672b8
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.7
name: Decrease RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.7 - Decrease RateLimits [Core]

The operator must, for each token collected in a non-zero amount, decrease the `LIMIT_UNISWAP_V3_WITHDRAW` rate limit for that token and `pool` pair by the amount collected.

`if (amount0Collected > 0) {
            context.rateLimits.triggerRateLimitDecrease(
                RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token0, context.pool),
                amount0Collected
            );
        }
        if (amount1Collected > 0) {
            context.rateLimits.triggerRateLimitDecrease(
                RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token1, context.pool),
                amount1Collected
            );
        }
    }`
