---
id: 33a7389c-c8a3-46ab-96a4-17d6b9ee2b4f
docNo: A.6.1.1.1.3.5.3.1.2
name: Operational Process
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.5.3.1.2 - Operational Process [Core]

The Spark Prime Relayer Multisig will execute transactions to ensure liquidity within Spark Savings vaults is aligned with the Target Liquidity configurations specified in Target Liquidity Current Configuration, up to the total amount of user deposits in a given Spark Savings vault. This will be implemented via control of the taker role in the vault and transferAsset rate limit from Spark Liquidity Layer ALM Proxy to the vault.

In normal conditions, this will be automated via the ALM Planner software. If the Prime Relayer Multisig fails to maintain Spark Savings vault liquidity in alignment with the Target Liquidity configurations, the Core Operator Relayer Multisig is empowered to effectuate transactions to achieve this.
