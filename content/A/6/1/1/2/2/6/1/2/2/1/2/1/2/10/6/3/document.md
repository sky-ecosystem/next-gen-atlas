---
id: 42ac9925-cdd6-4c01-b9c7-ab8ccbedd8f4
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.3
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.3 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for the cooldown. Because the resulting `cooldownAmount` of USDe is only known after the cooldown is initiated, the rate limit keyed on `LIMIT_SUSDE_COOLDOWN` is decreased at the end of the function using the resulting `cooldownAmount`.

`        rateLimits.triggerRateLimitDecrease(LIMIT_SUSDE_COOLDOWN, cooldownAmount);
    }`
