---
id: 42943bad-504a-4b59-9164-d6cc2acf6a95
docNo: A.6.1.1.2.2.6.1.3.1.4.2.3.2.3
name: Decrease RateLimit
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2.3 - Decrease RateLimit [Core]

The operator must decrease the `RateLimit`, effectively reducing the available `cooldown` limit, based on the `cooldownAmount`.

`rateLimits.triggerRateLimitDecrease(LIMIT_SUSDE_COOLDOWN, cooldownAmount);
}`
