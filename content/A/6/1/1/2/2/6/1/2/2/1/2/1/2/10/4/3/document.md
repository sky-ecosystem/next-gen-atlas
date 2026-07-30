---
id: ea08a00b-dc11-4793-a533-d23410b06b8f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.3
name: Approve USDe To Ethena Minter
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.3 - Approve USDe To Ethena Minter [Core]

The operator must approve the `ethenaMinter` to spend the `usdeAmount` of `usde` on behalf of the `proxy`. This step only sets the approval; the USDe redemption itself is executed off-contract by Ethena against this approval.

`        ERC20Lib.approve(proxy, address(usde), address(ethenaMinter), usdeAmount);
    }`
