---
id: 451ccaa5-640c-423d-b816-de953edbf115
docNo: A.6.1.1.6.2.6.1.2.2.3.4
name: USDS Burn Action
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.3.4 - USDS Burn Action [Core]

This document defines the action that should be performed if there is a need to repay and then burn Pattern's USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](886d04ba-23c3-45fb-ac5d-044288a621e1).
