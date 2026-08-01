---
id: 69b6ebfe-0a0a-4252-bc99-9e4df4dde4b1
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for redeeming the required amount, keyed on `LIMIT_USDE_BURN`, and the rate limit is decreased before the approval is set. Note that Ethena's per-block redeem limits are shared with other users, so a redemption may still fail even when the `RateLimits` allow the `usdeAmount`.

`        _rateLimited(LIMIT_USDE_BURN, usdeAmount);`
