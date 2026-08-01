---
id: b900fd43-5f7c-438f-a1dd-0e89db98f4db
docNo: A.2.2.10.1.1.1.5.2.2.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.2.2 - Rate Limit [Core]

The burning of USDS is subject to the on-chain rate limit identified by `LIMIT_USDS_BURN`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit. The burn additionally increases the `LIMIT_USDS_MINT` rate limit by the same amount, where that rate limit is configured, restoring minting capacity.
