---
id: da1d0829-5676-4713-988f-13eea2a6924f
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.6
name: Swap USDS To DAI
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.6 - Swap USDS To DAI [Core]

The operator must swap USDS to DAI. USDS is swapped to DAI in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
    address(daiUsds),
    abi.encodeCall(daiUsds.usdsToDai, (address(proxy), usdsAmount))
);`
