---
id: 8efb0a11-b798-48eb-af19-f65b38f039b5
docNo: A.2.2.9.1.1.1.2.2
name: Rate Limits
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.1.2.2 - Rate Limits [Core]

Rate limits set the maximum allowable amount of tokens that can be processed for specific operations within a given time period. Each rate limit contains the rate limit data: `maxAmount`, `slope`, `lastAmount` and `lastUpdated`. The current rate limit is calculated using the formula:

`currentRateLimit = min(slope * (block.timestamp - lastUpdated) + lastAmount, maxAmount)`.

The rate limit data `maxAmount` and `slope` are configurable parameters that are set and modified by Governance. The rate limit data `lastAmount` and `lastUpdated` are internal state data dynamically tracked by the Rate Limiter to perform its calculations.

Rate limits set caps on the rate of allocation to a given Instance, they do not act as a limit on the total amount that may be allocated to that Instance.
