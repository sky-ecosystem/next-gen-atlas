---
id: 8730991d-81ee-42f1-9a0e-0225593e11de
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.5
name: Decrease Deposit Rate Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.5 - Decrease Deposit Rate Limit [Core]

The operator must decrease the `LIMIT_CURVE_DEPOSIT` rate limit for the `pool` by the aggregated value deposited, before liquidity is added.

`params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.addLiquidityRateLimitId, params.pool),
            valueDeposited
        );`
