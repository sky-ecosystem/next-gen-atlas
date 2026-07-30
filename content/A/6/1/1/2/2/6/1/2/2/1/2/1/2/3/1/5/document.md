---
id: 348d05d6-74cb-484e-85dc-68bbce3e97df
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5
name: Swap USDS To DAI
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5 - Swap USDS To DAI [Core]

The operator must swap USDS to DAI. USDS is converted to DAI at a 1:1 ratio through the `daiUsds` migrator and returned to the `proxy`.

`params.proxy.doCall(
            address(params.daiUsds),
            abi.encodeCall(params.daiUsds.usdsToDai, (address(params.proxy), usdsAmount))
        );`
