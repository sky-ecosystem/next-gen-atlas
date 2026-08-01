---
id: 40842834-d8eb-455f-b69f-f57d5f1ae330
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.3
name: Set The Pool TWAP Seconds Ago
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.3 - Set The Pool TWAP Seconds Ago [Core]

The operator must set the `twapSecondsAgo` on the pool's `UniswapV3PoolParams`, which defines the length of the time-weighted average price window used when the contract consults the `pool`.

`        params.twapSecondsAgo = twapSecondsAgo;`
