---
id: e3993529-77fc-4b49-ab37-d3510dff56fb
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.7
name: Decrease Swap Rate Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.7 - Decrease Swap Rate Limit [Core]

The operator must compute the swap implied by the imbalance between the deposited amounts and the value of the minted shares, then decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by this implied `averageSwap`, after liquidity is added.

`uint256 totalSwapped;
        for (uint256 i; i < params.depositAmounts.length; i++) {
            totalSwapped += MathLib._absSubtraction(
                curvePool.balances(i) * rates[i] * shares / curvePool.totalSupply(),
                params.depositAmounts[i] * rates[i]
            );
        }
        uint256 averageSwap = totalSwapped / 2 / 1e18;

        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.swapRateLimitId, params.pool),
            averageSwap
        );
    }`
