---
id: 58bd2f3d-0d7e-41e9-a3f1-43e8deedaea9
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.8
name: Swap DAI To USDC
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.8 - Swap DAI To USDC [Core]

The operator must swap DAI to USDC. DAI is swapped to USDC in the PSM at a 1:1 ratio with no fee, using the `buyGemNoFee` function and return USDC to the `proxy`.

`        proxy.doCall(
            address(psm),
            abi.encodeCall(psm.buyGemNoFee, (address(proxy), usdcAmount))
        );
    }`
