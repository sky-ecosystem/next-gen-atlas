---
id: 12b79490-4a18-466b-91fc-45f1a966b78a
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.10
name: Convert USDC Amount To DAI Amount
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.10 - Convert USDC Amount To DAI Amount [Core]

The operator must convert the USDC amount to the DAI amount, accounting for the token decimal difference.

`{
        uint256 daiAmount = usdcAmount * psmTo18ConversionFactor;`
