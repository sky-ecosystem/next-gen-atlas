---
id: 0e02d0f4-a9b1-4f2f-8016-274c26db9fa2
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.7
name: Swap DAI To USDC
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.7 - Swap DAI To USDC [Core]

The operator must swap DAI to USDC. DAI is exchanged for USDC through the PSM at a 1:1 ratio with no fee, using `buyGemNoFee`, and the USDC is returned to the `proxy`.

`params.proxy.doCall(
            address(params.psm),
            abi.encodeCall(params.psm.buyGemNoFee, (address(params.proxy), params.usdcAmount))
        );`
