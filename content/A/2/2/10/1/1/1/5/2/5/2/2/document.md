---
id: a60193f3-3af2-4a50-a42d-4b2dad8adc6a
docNo: A.2.2.10.1.1.1.5.2.5.2.2
name: Rate Limit
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.2.2 - Rate Limit [Core]

The aggregate withdrawal limit sums one unit of either pool token as equivalent, so it is only meant to work with a stable-stable pool. Using it on a pool with two tokens of different value would produce a cap unrelated to actual exposure.

Removing liquidity is subject to three (3) on-chain withdrawal rate limits, each identified by `LIMIT_UNISWAP_V3_WITHDRAW`. One is the aggregate limit described above, metered in a normalized unit summed across both pool tokens. The other two are per-token limits, one for each of the pool's two (2) tokens, each metered in that token's own unit. All three limits are enforced automatically within the call; the transaction reverts if the amount attributed to any of the three exceeds its current rate limit.

These limits meter only the amount returned by decreasing liquidity. Fees already accrued on the position are collected in the same call but are not counted against them.
