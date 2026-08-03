---
id: f64c4f1d-f7e3-4673-a43a-6891892a8d0d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.7
name: Swap DAI To USDS
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.7 - Swap DAI To USDS [Core]

The operator must swap DAI to USDS. DAI is converted to USDS at a 1:1 ratio through the `daiUsds` migrator and returned to the `proxy`.

`params.proxy.doCall(
            address(params.daiUsds),
            abi.encodeCall(params.daiUsds.daiToUsds, (address(params.proxy), daiAmount))
        );`
