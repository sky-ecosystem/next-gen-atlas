---
id: 462537ca-626a-4516-afd6-a3a344d1e241
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.2
name: Refund RateLimit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.2 - Refund RateLimit [Core]

The operator does not consume a rate limit in this direction. Instead, `PSMLib.swapUSDCToUSDS` cancels usage of the opposite direction's limit: it increases the `LIMIT_USDS_TO_USDC` rate limit by `usdcAmount`, refunding capacity that a prior USDS-to-USDC swap had consumed.

`_cancelRateLimit(params.rateLimits, params.rateLimitId, params.usdcAmount);`

The helper increases the limit keyed by `LIMIT_USDS_TO_USDC`.

`function _cancelRateLimit(IRateLimits rateLimits, bytes32 key, uint256 amount) internal {
        rateLimits.triggerRateLimitIncrease(key, amount);
    }`
