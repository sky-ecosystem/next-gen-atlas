---
id: 5159b62c-b5c3-4a5e-b788-fe89550bb120
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for minting the required amount, keyed on `LIMIT_USDE_MINT`, and the rate limit is decreased before the approval is set. Note that Ethena's per-block mint limits are shared with other users, so a mint may still fail even when the `RateLimits` allow the `usdcAmount`.

`        _rateLimited(LIMIT_USDE_MINT, usdcAmount);`
