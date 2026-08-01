---
id: 4d815893-dcbd-4321-97c0-c377c5a4565e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.4
name: Enforce Minimum LP Amount
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.4 - Enforce Minimum LP Amount [Core]

The operator must ensure `minLpAmount` is at least the aggregated deposit value scaled by `maxSlippage` and the pool's `get_virtual_price`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`require(
            params.minLpAmount >= valueDeposited
                * params.maxSlippage
                / curvePool.get_virtual_price(),
            "CurveLib/min-amount-not-met"
        );`
