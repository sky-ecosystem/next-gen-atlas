---
id: 23770b76-5a1f-49d2-b970-dbf908c05817
docNo: A.6.1.1.3.2.6.1.2.2.1.3.3
name: USDC to USDS Swap Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.3.3 - USDC to USDS Swap Action [Core]

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS. The operator must call the `swapUSDCToUSDS` function.

The function call is as follows:

`function swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2 - Swap USDC To USDS](da2164e3-03bc-447c-89c5-119d01feddaa).
