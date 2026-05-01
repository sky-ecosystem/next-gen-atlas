---
id: 25fac618-a634-4762-983d-c3451e690f5f
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.12
name: Swap DAI to USDS
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.12 - Swap DAI to USDS [Core]

The operator must swap DAI to USDS. DAI is swapped to USDS at a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.daiToUsds, (address(proxy), daiAmount))
        );
    }`
