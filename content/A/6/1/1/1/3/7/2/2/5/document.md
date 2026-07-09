---
id: 5ac93594-d197-4fac-b5ca-6bc9b7f10bed
docNo: A.6.1.1.1.3.7.2.2.5
name: Decentralized Exchange Protocols
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.7.2.2.5 - Decentralized Exchange Protocols [Core]

Approved onchain spot decentralized exchange protocols may be included within position margin calculations, under the following conditions: (1) all assets to which a pool has exposure are approved as marginable assets, and (2) the protocol is either Curve-ng stableswap, Uniswap v2, Uniswap v3, Uniswap v4 vanilla (no hooks), or Uniswap v4 using hook(s) that have been onboarded via direct integration within the Spark Liquidity Layer. If one or more of these conditions is not met in full, the pool is treated as an unapproved asset/product.
