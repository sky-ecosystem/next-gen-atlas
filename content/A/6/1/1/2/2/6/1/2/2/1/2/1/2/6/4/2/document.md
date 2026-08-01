---
id: ab6e2866-3bd7-4663-bc17-99dd8e72475d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.2 - Check RateLimits [Core]

The operator must ensure a rate limit is configured for redeeming this `token` from the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_REDEEM, token));`
