---
id: 0b3c6086-9e48-4587-a182-59ddf73000e2
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.5
name: Convert To 18 Token Format
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.5 - Convert To 18 Token Format [Core]

The operator must convert the 6-decimal `usdcAmount` into the 18-decimal `daiAmount` using `psmTo18ConversionFactor`, since DAI and USDS are denominated in 18 decimals.

`uint256 daiAmount = params.usdcAmount * params.psmTo18ConversionFactor;`
