---
id: e3f04b74-9b6d-45e9-9363-e76bda9ba6dc
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.2 - Check RateLimits [Core]

The operator's call decreases the `LIMIT_USDS_MINT` rate limit by `usdsAmount`, consuming available mint capacity. Internally `_rateLimited` calls `rateLimits.triggerRateLimitDecrease(LIMIT_USDS_MINT, usdsAmount)`, which reverts if `usdsAmount` exceeds the currently available limit.

`_rateLimited(LIMIT_USDS_MINT, usdsAmount);`
