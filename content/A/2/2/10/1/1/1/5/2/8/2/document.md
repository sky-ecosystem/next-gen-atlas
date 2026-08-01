---
id: b489a966-f631-429d-85da-cb6258f001c9
docNo: A.2.2.10.1.1.1.5.2.8.2
name: Rate Limit
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.8.2 - Rate Limit [Core]

The swap is subject to the on-chain rate limit identified by `LIMIT_USDC_TO_USDS`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit. The swap additionally increases the `LIMIT_USDS_TO_USDC` rate limit by the same amount, where that rate limit is configured, restoring capacity in the opposite swap direction.
