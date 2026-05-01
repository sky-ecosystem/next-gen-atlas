---
id: c30c1496-0eff-4199-9c18-eb72fb486aac
docNo: A.6.1.1.6.2.6.1.2.2.3.3
name: USDC To USDS Swap Action
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.3.3 - USDC To USDS Swap Action [Core]

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS. The operator must call the `swapUSDCToUSDS` function.

The function call is as follows:

`function swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.2 - Swap USDC To USDS](9d828ddb-7423-41cb-9adb-43d4cbfc9d38).
