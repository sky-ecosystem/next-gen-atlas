---
id: 2fbc62d7-432c-4913-bee2-82764adba306
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for transferring the required `amount` of the `asset` to the `destination`. The rate limit is keyed on the `asset` and `destination` pair through `makeAssetDestinationKey`.

`        _rateLimited(
            RateLimitHelpers.makeAssetDestinationKey(LIMIT_ASSET_TRANSFER, asset, destination),
            amount
        );`
