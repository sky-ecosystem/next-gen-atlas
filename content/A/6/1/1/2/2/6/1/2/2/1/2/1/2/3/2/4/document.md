---
id: 2c2b3e9a-5135-4379-bd4f-9f52884bd8da
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4 - Approve Contract Spend [Core]

The operator must approve the PSM to spend USDC. The approval is needed for the PSM to be able to execute a `swap` of USDC.

`proxy.doCall(
    address(usdc),
    abi.encodeCall(usdc.approve, (address(psm), usdcAmount))
);`
