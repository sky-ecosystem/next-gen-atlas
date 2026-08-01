---
id: 7ba1cc79-9a9f-460c-85b8-72181788397f
docNo: A.6.1.1.7.2.6.1.2.2.3.2
name: Withdraw All SparkLend Positions
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.7.2.6.1.2.2.3.2 - Withdraw All SparkLend Positions [Core]

In the event that liquidity must be recovered from SparkLend and centralized in the Osero ALM Proxy, a Relayer Multisig, acting as an Actor, withdraws the Osero Liquidity Layer's full SparkLend USDS position through the Aave Facet, as specified in [A.2.2.10.1.1.1.5.2.4 - Withdraw From Aave Market](038eaa5c-d4c0-4a56-8d30-bc3a04508f0e). SparkLend withdrawals are unlimited so that the full position can be unwound.
