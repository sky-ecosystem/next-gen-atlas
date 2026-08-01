---
id: 94dc3a5c-569d-4759-99d7-d5062f558937
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.2 - Check RateLimits [Core]

The operator must ensure that `RateLimits` allows for depositing the required `amount` of the asset into the ERC-7540 vault. The rate limit is keyed to the specific `token` and its available amount is decreased by the deposited `amount`. This rate limit also serves as the whitelist, since only vaults with a configured rate limit can be used.

`        _rateLimitedAsset(LIMIT_7540_DEPOSIT, token, amount);`
