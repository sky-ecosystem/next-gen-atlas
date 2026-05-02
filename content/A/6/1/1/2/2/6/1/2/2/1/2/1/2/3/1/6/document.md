---
id: 97c2db26-16e7-4aee-a257-86bef4189fa7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6
name: Swap USDS To DAI
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6 - Swap USDS To DAI [Core]

The operator must swap USDS to DAI. USDS is swapped to DAI in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
    address(daiUsds),
    abi.encodeCall(daiUsds.usdsToDai, (address(proxy), usdsAmount))
);`
