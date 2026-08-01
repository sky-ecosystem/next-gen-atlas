---
id: 6449fd5a-ec8b-4d71-aa03-7cac23780c2c
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.2 - Check RateLimits [Core]

Burning USDS restores previously consumed mint capacity. The operator's call increases (refunds) the `LIMIT_USDS_MINT` rate limit by `usdsAmount`, reversing the decrease applied when that USDS was minted. Internally `_cancelRateLimit` calls `rateLimits.triggerRateLimitIncrease(LIMIT_USDS_MINT, usdsAmount)`; it does not check or consume a separate burn allowance.

`_cancelRateLimit(LIMIT_USDS_MINT, usdsAmount);`
