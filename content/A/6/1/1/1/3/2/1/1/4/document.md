---
id: 38329b4f-7666-4f68-ba66-74ebb2e60e13
docNo: A.6.1.1.1.3.2.1.1.4
name: SparkLend Risk Parameters Kill Switch
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.1.1.4 - SparkLend Risk Parameters Kill Switch [Core]

The kill switch disables all borrowing across SparkLend markets in the event of a depeg on key collateral assets.

The kill switch is defined in terms of a threshold for specified pegged assets. If the ratio of the price of a specified asset to its peg is equal to or less than the threshold, then any user can trigger the kill switch to disable borrowing across all SparkLend markets.

After the kill switch is triggered, markets can be reactivated by Sky Governance after resetting the kill switch. Resetting the kill switch is subject to the Governance Security Delay specified in [A.1.9.3 - Governance Security Delay Requirements](c5f0e955-0441-42e0-a6fc-eab875bba568).
