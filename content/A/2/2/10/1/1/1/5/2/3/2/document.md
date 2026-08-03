---
id: 989bca9d-f56a-4965-8684-62de547f605a
docNo: A.2.2.10.1.1.1.5.2.3.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.3.2 - Rate Limit [Core]

The deposit is subject to the on-chain deposit rate limit identified by `LIMIT_AAVE_DEPOSIT` for the underlying asset, the address of the pool, and the address of the aToken. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.
