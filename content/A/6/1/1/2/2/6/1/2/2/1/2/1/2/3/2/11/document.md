---
id: fda81f79-1689-40f8-b971-95e314a0ec16
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.11
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.11 - Approve Contract Spend [Core]

The operator must approve the `daiUsds` contract to spend the `daiAmount` on behalf of the `proxy`.

`proxy.doCall(
    address(dai),
    abi.encodeCall(dai.approve, (address(daiUsds), daiAmount))
);`
