---
id: b1d47385-8512-475a-8860-9ae927677785
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.4
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.4 - Approve Contract Spend [Core]

The operator must approve the PSM to spend USDC. The approval is needed for the PSM to be able to execute a `swap` of USDC.

`proxy.doCall(
    address(usdc),
    abi.encodeCall(usdc.approve, (address(psm), usdcAmount))
);`
