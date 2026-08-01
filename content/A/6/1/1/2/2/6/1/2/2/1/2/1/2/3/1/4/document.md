---
id: c4b00dec-4cc9-49e8-97d1-a5c64560c8ce
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.4
name: Approve Migrator Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.4 - Approve Migrator Spend [Core]

The operator must approve the `daiUsds` migrator to spend `usdsAmount` of USDS on behalf of the `proxy`. `daiUsds` is the contract that facilitates a 1:1 swap between USDS and DAI. The operation assumes the `proxy` holds enough USDS.

`ERC20Lib.approve(params.proxy, address(params.usds), address(params.daiUsds), usdsAmount);`
