---
id: cae48a72-fa6d-439e-88fd-1dc37f499101
docNo: A.6.1.1.1.3.5.3.1.2.1
name: Savings Liquidity Intents
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.5.3.1.2.1 - Savings Liquidity Intents [Core]

Spark Savings will enable users to withdraw amounts exceeding the standard Target Liquidity buffer via Savings Liquidity Intents. Users may submit signed withdrawal intents indicating their intent to redeem Spark Savings vault tokens in amounts exceeding the standard Target Liquidity buffer. Subject to available liquidity within the Spark Liquidity Layer and underlying asset allocations, the Spark Liquidity Layer planner may automatically trigger transactions through the Spark Prime Relayer infrastructure to fulfill such intents. Fulfillment of withdrawal intents is not guaranteed. Withdrawal intents may be replaced or cancelled by submitting a superseding signed intent with the same nonce. Intents that have passed their deadline timestamp may not be executed.
