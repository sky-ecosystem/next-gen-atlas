---
id: 835ceecc-82b0-4c00-8ba3-86d5a8cd782e
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.7
name: Decrease RateLimit
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.7 - Decrease RateLimit [Core]

The operator must decrease the `RateLimit` based on the assets redeemed.

`rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
            amountWithdrawn
        );
    }`
