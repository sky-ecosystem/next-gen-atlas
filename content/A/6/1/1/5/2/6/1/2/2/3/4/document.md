---
id: 3304ecba-6dad-45af-886e-878648d2abb8
docNo: A.6.1.1.5.2.6.1.2.2.3.4
name: USDS Burn Action
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.3.4 - USDS Burn Action [Core]

This document defines the action that should be performed if there is a need to repay and then burn Obex's USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](1e27b007-ed34-4c15-9116-d62145572dce).
