---
id: a07d408e-d0d1-4386-bdf3-a7b9f00b5e3e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.4
name: Enforce Minimum Output
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.4 - Enforce Minimum Output [Core]

The operator must ensure `minAmountOut` is at least the minimum output implied by the pool's `stored_rates` and the configured `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 minimumMinAmountOut = params.amountIn
            * rates[params.inputIndex]
            * params.maxSlippage
            / rates[params.outputIndex]
            / 1e18;

        require(
            params.minAmountOut >= minimumMinAmountOut,
            "CurveLib/min-amount-not-met"
        );`
