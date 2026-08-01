---
id: 612346e6-7a94-4409-a05d-63e02fa6b6a2
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for cooling down the required amount, keyed on `LIMIT_SUSDE_COOLDOWN`, and the rate limit is decreased before the cooldown is initiated.

`        _rateLimited(LIMIT_SUSDE_COOLDOWN, usdeAmount);`
