---
id: e5b56658-1fe0-4d3f-b911-8e66b9d16a6e
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.7
name: Approve PSM Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.7 - Approve PSM Spend [Core]

The operator must approve the PSM to spend the newly acquired DAI. The approval is needed for the PSM to be able to `swap` DAI for USDC.

`proxy.doCall(
    address(dai),
    abi.encodeCall(dai.approve, (address(psm), usdsAmount))
);`
