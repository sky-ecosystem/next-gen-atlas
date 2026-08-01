---
id: a75cdaf7-8ad5-41aa-84c3-2d80a1d09495
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.6
name: Decrease Withdraw Rate Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.6 - Decrease Withdraw Rate Limit [Core]

The operator must aggregate the value of the withdrawn tokens using the pool's `stored_rates`, then decrease the `LIMIT_CURVE_WITHDRAW` rate limit for the `pool` by this value, after liquidity is removed.

`uint256 valueWithdrawn;
        for (uint256 i = 0; i < withdrawnTokens.length; i++) {
            valueWithdrawn += withdrawnTokens[i] * rates[i];
        }
        valueWithdrawn /= 1e18;

        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, params.pool),
            valueWithdrawn
        );
    }`
