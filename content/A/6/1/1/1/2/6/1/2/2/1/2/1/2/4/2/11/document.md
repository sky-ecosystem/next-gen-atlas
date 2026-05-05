---
id: 3cf7c26f-7c3b-4d32-8610-b935d57721a6
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.11
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.11 - Approve Contract Spend [Core]

The operator must approve the `daiUsds` contract to spend the `daiAmount` on behalf of the `proxy`.

`proxy.doCall(
    address(dai),
    abi.encodeCall(dai.approve, (address(daiUsds), daiAmount))
);`
