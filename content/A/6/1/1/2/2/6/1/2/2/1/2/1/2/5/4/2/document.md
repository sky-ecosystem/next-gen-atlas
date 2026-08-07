---
id: c0dd6e35-13bb-4a42-8694-48a84c06a91e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.2 - Check RateLimits [Core]

The operator must ensure that a rate limit exists for redeeming from the ERC-7540 vault. This is an existence check only: it requires the `LIMIT_7540_REDEEM` rate limit keyed to the `token` to have a non-zero `maxAmount`, reverting otherwise, and it neither decreases nor increases the available amount. This confirms the vault is whitelisted before assets are claimed.

`        _rateLimitExists(RateLimitHelpers.makeAssetKey(LIMIT_7540_REDEEM, token));`
