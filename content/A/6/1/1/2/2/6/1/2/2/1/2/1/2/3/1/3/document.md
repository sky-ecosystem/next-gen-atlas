---
id: aa417e52-f42f-4653-a820-e0cdafac9aea
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3
name: Convert To 18 Token Format
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3 - Convert To 18 Token Format [Core]

The operator must convert USDC amounts to an 18 token decimal format using `psmTo18ConversionFactor`.

`{
        uint256 usdsAmount = usdcAmount * psmTo18ConversionFactor;`
