---
id: d2bd2910-494c-4a4e-b276-8f325c69e36b
docNo: A.2.2.10.1.1.1.5.2.5.3.2
name: Rate Limit
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.3.2 - Rate Limit [Core]

The swap is subject to the on-chain rate limit identified by `LIMIT_UNISWAP_V3_SWAP` for the address of the token being sold and the address of the pool. This limit is enforced automatically within the call; the transaction reverts if the amount sold exceeds the current rate limit.
