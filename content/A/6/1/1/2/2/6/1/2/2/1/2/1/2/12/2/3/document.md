---
id: 30349bb4-c5b0-44e0-b60c-0d83f29fa297
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.3
name: Swap DAI To USDS
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.3 - Swap DAI To USDS [Core]

The operator must swap DAI to USDS. DAI is swapped to USDS in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`        // Swap DAI to USDS 1:1
        proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.daiToUsds, (address(proxy), daiAmount))
        );
    }`
