---
id: 532d5769-4224-48c0-9282-9c19e9fe6455
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.2 - Check RateLimits [Core]

The operator must ensure that `RateLimits` allows swapping the requested USDC amount. `PSMLib.swapUSDSToUSDC` consumes the `LIMIT_USDS_TO_USDC` rate limit by triggering a decrease of `usdcAmount`, which reverts if the remaining limit is insufficient.

`_rateLimited(params.rateLimits, params.rateLimitId, params.usdcAmount);`

The helper decreases the limit keyed by `LIMIT_USDS_TO_USDC`.

`function _rateLimited(IRateLimits rateLimits,bytes32 key, uint256 amount) internal {
        rateLimits.triggerRateLimitDecrease(key, amount);
    }`
