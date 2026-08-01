---
id: aa417e52-f42f-4653-a820-e0cdafac9aea
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3
name: Convert To 18 Token Format
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3 - Convert To 18 Token Format [Core]

The operator must convert the 6-decimal `usdcAmount` into the 18-decimal `usdsAmount` using `psmTo18ConversionFactor`, since USDS and DAI are denominated in 18 decimals.

`uint256 usdsAmount = params.usdcAmount * params.psmTo18ConversionFactor;`
