---
id: f7ef5ebb-e30e-4941-918c-63706690b7e0
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.5
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.5 - Approve Contract Spend [Core]

The operator must approve the CCTP to spend USDC on behalf of the `proxy`. This action is necessary for the CCTP contract to initiate the cross-chain transfer.

`proxy.doCall(
    address(usdc),
    abi.encodeCall(usdc.approve, (address(cctp), usdcAmount))
);`
