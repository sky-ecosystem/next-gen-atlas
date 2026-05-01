---
id: e5e9c15f-dd74-44c3-b6fc-e9855a66bcba
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.3
name: Check RateLimits
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.3 - Check RateLimits [Core]

The operator must ensure the `withdraw` amount is allowed within the `RateLimits`.

`// Check withdrawal limits.
rateLimited(
RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
amount
)`
