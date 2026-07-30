---
id: 2ace0a4a-e569-40de-b5f0-8d69d43843bb
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for depositing the required `amount` of the underlying asset. The limit is keyed per `aToken` through `makeAssetKey(LIMIT_AAVE_DEPOSIT, aToken)`, and the rate limit is decreased before the deposit is performed.

`        _rateLimitedAsset(LIMIT_AAVE_DEPOSIT, aToken, amount);`
