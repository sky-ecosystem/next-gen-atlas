---
id: fd3a1c0a-631c-46a7-bac3-6a8d05afa58e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.6
name: Validate Minimum Amounts
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.6 - Validate Minimum Amounts [Core]

The operator must ensure each `min` amount is at least the collected balance delta scaled by `maxSlippage`, so the withdrawal does not settle below the acceptable bound.

`require(params.min.amount0 >= (amount0CollectedAfter - amount0CollectedBefore) * params.maxSlippage / 1e18, "UniswapV3Lib/min-amount-below-bound");
        require(params.min.amount1 >= (amount1CollectedAfter - amount1CollectedBefore) * params.maxSlippage / 1e18, "UniswapV3Lib/min-amount-below-bound");`
