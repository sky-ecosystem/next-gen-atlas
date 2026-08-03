---
id: 97c2db26-16e7-4aee-a257-86bef4189fa7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6
name: Approve PSM Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6 - Approve PSM Spend [Core]

The operator must approve the PSM to spend the newly acquired DAI on behalf of the `proxy`. The approved amount equals `usdsAmount` because the conversion from USDS to DAI was 1:1.

`ERC20Lib.approve(params.proxy, address(params.dai), address(params.psm), usdsAmount);`
