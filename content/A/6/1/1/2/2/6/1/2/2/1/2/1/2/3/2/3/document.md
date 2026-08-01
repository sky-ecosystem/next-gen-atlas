---
id: f5d1b5d7-3968-4b49-99ff-21d7e3a5d2b7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.3
name: Approve PSM Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.3 - Approve PSM Spend [Core]

The operator must approve the PSM to spend `usdcAmount` of USDC on behalf of the `proxy`. The operation assumes the `proxy` holds enough USDC.

`ERC20Lib.approve(params.proxy, address(params.usdc), address(params.psm), params.usdcAmount);`
