---
id: 348d05d6-74cb-484e-85dc-68bbce3e97df
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5 - Approve Contract Spend [Core]

The operator must approve the `daiUsds` contract to spend the `usdsAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between USDS and DAI.

`proxy.doCall(
            address(usds),
            abi.encodeCall(usds.approve, (address(daiUsds), usdsAmount))
        );`
