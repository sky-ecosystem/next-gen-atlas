---
id: efebd3e3-ff1e-49ba-8402-8a3280cc74f0
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.2 - Check RateLimits [Core]

The operator must ensure a rate limit is configured for depositing this `token` into the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_DEPOSIT, token));`
