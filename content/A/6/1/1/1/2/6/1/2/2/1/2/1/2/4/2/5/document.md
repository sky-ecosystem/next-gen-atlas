---
id: f16d98d9-dbba-44ab-8764-445693b81ff5
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.5
name: Calculate Swap Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.5 - Calculate Swap Limit [Core]

The operator must calculate the `swap` `limit` per transaction. The maximum amount of USDC that can be swapped to DAI in one transaction is calculated based on the DAI balance held by the PSM. `psmTo18ConversionFactor` converts DAI’s 18 token decimals to USDC’s 6 token decimals.

`uint256 limit = dai.balanceOf(address(psm)) / psmTo18ConversionFactor;`
