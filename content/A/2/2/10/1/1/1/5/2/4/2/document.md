---
id: ef6077eb-1cd4-4c17-bbf5-ce98c2cc1b92
docNo: A.2.2.10.1.1.1.5.2.4.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.4.2 - Rate Limit [Core]

The withdrawal is subject to the on-chain withdrawal rate limit identified by `LIMIT_AAVE_WITHDRAW` for the address of the pool and the address of the aToken. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.
