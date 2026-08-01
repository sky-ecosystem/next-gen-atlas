---
id: c1a41667-2cf5-4794-91cc-718d593e4fef
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.4
name: Enforce Minimum Withdrawal Value
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.4 - Enforce Minimum Withdrawal Value [Core]

The operator must ensure the aggregated minimum withdrawal value is at least `lpBurnAmount` scaled by the pool's `get_virtual_price` and `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`require(
            valueMinWithdrawn >= params.lpBurnAmount
                * curvePool.get_virtual_price()
                * params.maxSlippage
                / 1e36,
            "CurveLib/min-amount-not-met"
        );`
