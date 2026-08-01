---
id: b845955c-8963-4234-af56-569cd65bb4bb
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.4
name: Update RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.4 - Update RateLimits [Core]

The operator must decrease the `RateLimits` by the `amountWithdrawn` after the withdrawal completes. The limit is keyed per `aToken` through `makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken)`, so `withdrawAave` is rate limited at the end of the function rather than before.

`        rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
            amountWithdrawn
        );
    }`
