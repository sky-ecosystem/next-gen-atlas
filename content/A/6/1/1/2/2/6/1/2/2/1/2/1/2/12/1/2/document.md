---
id: c4ca6c96-3daf-4a05-b19b-2bce3243a735
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.2
name: Approve USDS To Migrator
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.2 - Approve USDS To Migrator [Core]

The operator must approve the `daiUsds` migrator to spend the `usdsAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between USDS and DAI. This assumes the `proxy` holds enough USDS.

`    {
        // Approve USDS to DaiUsds migrator from the proxy (assumes the proxy has enough USDS)
        ERC20Lib.approve(proxy, address(usds), address(daiUsds), usdsAmount);`
