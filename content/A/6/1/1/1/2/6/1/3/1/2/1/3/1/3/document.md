---
id: bda7b89b-9065-4fa0-b7c1-903ef0b9a41b
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.3
name: Check RateLimits
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.3 - Check RateLimits [Core]

The operator must ensure the `deposit` amount is allowed within the `RateLimits`.

        `rateLimited(
RateLimitHelpers.makeAssetKey(LIMIT_AAVE_DEPOSIT, aToken),
amount
)`
