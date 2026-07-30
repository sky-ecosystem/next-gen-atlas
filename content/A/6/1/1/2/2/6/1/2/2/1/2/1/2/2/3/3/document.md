---
id: 6370eada-cbd1-4bc1-8ba4-d985b05b1a21
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.3
name: Decrease Withdraw Rate Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.3 - Decrease Withdraw Rate Limit [Core]

The operator must decrease the `LIMIT_4626_WITHDRAW` rate limit for the `token` by the actual `assets` received, after the redemption is executed. The rate limit is keyed to the `token` through `makeAssetKey`. Because redemption is limited by the same rate limit as withdrawal, the redeemed value counts against the shared withdraw allowance.

`        rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_4626_WITHDRAW, token),
            assets
        );`
