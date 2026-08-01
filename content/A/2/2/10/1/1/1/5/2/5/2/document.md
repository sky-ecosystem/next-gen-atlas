---
id: 34b6d2ab-837c-4fb0-a397-77d776a32bc3
docNo: A.2.2.10.1.1.1.5.2.5.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.2 - Rate Limit [Core]

The deposit is subject to the on-chain deposit rate limit identified by `LIMIT_BASIN_DEPOSIT` for the address of the asset and the address of the Basin contract. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.
