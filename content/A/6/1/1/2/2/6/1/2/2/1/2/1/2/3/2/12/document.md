---
id: 77750a12-c615-4ffd-a05b-4c58f9d6277a
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.12
name: Swap DAI to USDS
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.12 - Swap DAI to USDS [Core]

The operator must swap DAI to USDS. DAI is swapped to USDS at a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.daiToUsds, (address(proxy), daiAmount))
        );
    }`
