---
id: d23acaaf-29b8-4a8b-a5a8-40e24238c892
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.7
name: Decrease RateLimit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.7 - Decrease RateLimit [Core]

The operator must decrease the `LIMIT_UNISWAP_V3_SWAP` rate limit for the `tokenIn` and `pool` pair by the amount of `tokenIn` actually spent, which is the difference between the starting and ending balances.

`context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, params.tokenIn, context.pool),
            startingBalance - endingBalance
        );
    }`
