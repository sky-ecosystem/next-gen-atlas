---
id: 3c47986f-3a20-4593-b4c1-cd5f8a0837c8
docNo: A.6.1.1.1.2.6.1.2.2.3.3.1
name: USDC Bridging Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.3.1 - USDC Bridging Action [Core]

In order to bridge USDC, the operator must execute the following action:

`foreignController.transferUSDCToCCTP(usdc.balanceOf(address(proxy)), 0);
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol](956f0941-5121-4dce-99d8-2fd1af00ffa6).
