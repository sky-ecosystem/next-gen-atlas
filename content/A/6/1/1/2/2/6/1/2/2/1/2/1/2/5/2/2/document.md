---
id: 637a65c8-84a6-4670-b782-1bed08475969
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.2 - Check RateLimits [Core]

The operator must ensure that a rate limit exists for depositing into the ERC-7540 vault. This is an existence check only: it requires the `LIMIT_7540_DEPOSIT` rate limit keyed to the `token` to have a non-zero `maxAmount`, reverting otherwise, and it neither decreases nor increases the available amount. This confirms the vault is whitelisted before shares are claimed.

`        _rateLimitExists(RateLimitHelpers.makeAssetKey(LIMIT_7540_DEPOSIT, token));`
