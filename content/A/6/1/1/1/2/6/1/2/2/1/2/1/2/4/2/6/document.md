---
id: 6a6ddd58-9215-4dae-9d34-8bd4622720bd
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.6
name: Swap USDC To DAI Directly If Possible
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.6 - Swap USDC To DAI Directly If Possible [Core]

The operator must perform a `direct swap` feasibility check and `swap` USDC to DAI, if possible. If the `usdcAmount` is less than or equal to the `limit`, a direct swap should be performed. `_swapUSDCToDAI` is called to execute the swap from `USDC` to `DAI`.

`if (usdcAmount <= limit) {
    _swapUSDCToDAI(usdcAmount);
}`
