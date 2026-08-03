---
id: f060c012-dad4-4509-8ed8-1d68a88b7ca7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.6
name: Approve Migrator Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.6 - Approve Migrator Spend [Core]

The operator must approve the `daiUsds` migrator to spend `daiAmount` of DAI on behalf of the `proxy`. `daiUsds` is the contract that facilitates a 1:1 swap between DAI and USDS. The operation assumes the `proxy` holds enough DAI.

`ERC20Lib.approve(params.proxy, address(params.dai), address(params.daiUsds), daiAmount);`
