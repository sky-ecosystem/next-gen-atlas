---
id: e549765f-8494-4842-875d-a206131c9daa
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.2
name: Approve DAI To Migrator
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.2 - Approve DAI To Migrator [Core]

The operator must approve the `daiUsds` migrator to spend the `daiAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between DAI and USDS. This assumes the `proxy` holds enough DAI.

`    {
        // Approve DAI to DaiUsds migrator from the proxy (assumes the proxy has enough DAI)
        ERC20Lib.approve(proxy, address(dai), address(daiUsds), daiAmount);`
