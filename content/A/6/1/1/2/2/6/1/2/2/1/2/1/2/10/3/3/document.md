---
id: 4ac9dee5-c673-4061-a636-702b3da8fbe5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.3
name: Approve USDC To Ethena Minter
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.3 - Approve USDC To Ethena Minter [Core]

The operator must approve the `ethenaMinter` to spend the `usdcAmount` of `usdc` on behalf of the `proxy`. This step only sets the approval; the USDe mint itself is executed off-contract by Ethena against this approval.

`        ERC20Lib.approve(proxy, address(usdc), address(ethenaMinter), usdcAmount);
    }`
