---
id: 44ca2425-03dd-4913-919a-666a77854709
docNo: A.6.1.1.3.2.6.1.2.2.1.3.4
name: USDS Burn Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.3.4 - USDS Burn Action [Core]

This document defines the action that should be performed if there is a need to repay and then burn Keel’s USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2 - Burn USDS](9c9536a8-bb2d-4d37-98cf-4c25a5699026).
