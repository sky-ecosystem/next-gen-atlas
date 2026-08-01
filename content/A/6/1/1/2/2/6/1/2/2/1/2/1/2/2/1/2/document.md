---
id: 36c94503-8627-4eab-baba-e257c8796514
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.2 - Check RateLimits [Core]

The operator must ensure that `RateLimits` allow for depositing the required `amount` of the asset into the ERC-4626 vault. The rate limit is keyed to the specific `token` through `makeAssetKey`, and its available amount is decreased by the deposited `amount`. This rate limit also serves as the whitelist, since only vaults with a configured rate limit can be used.

`        _rateLimitedAsset(LIMIT_4626_DEPOSIT, token, amount);`
