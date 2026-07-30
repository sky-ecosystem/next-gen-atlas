---
id: d915bc35-e8d8-4d48-a285-92335bd09343
docNo: A.2.2.10.1.1.1.5.2.6.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.6.2 - Rate Limit [Core]

The withdrawal is subject to the on-chain withdrawal rate limit identified by `LIMIT_BASIN_WITHDRAW` for the address of the asset and the address of the Basin contract. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.
