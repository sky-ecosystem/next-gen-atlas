---
id: 904ecbac-b3a5-4c79-8afc-a9218c3b38e4
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.3
name: Swap USDS To DAI
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.3 - Swap USDS To DAI [Core]

The operator must swap USDS to DAI. USDS is swapped to DAI in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`        // Swap USDS to DAI 1:1
        proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.usdsToDai, (address(proxy), usdsAmount))
        );
    }`
