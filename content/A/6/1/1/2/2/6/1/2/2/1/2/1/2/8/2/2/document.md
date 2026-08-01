---
id: 88916197-b09b-4a25-8ecb-1fb2221b2951
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.2
name: Validate Deposit Amounts
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.2 - Validate Deposit Amounts [Core]

The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`. They must also ensure the length of `depositAmounts` matches the pool's `N_COINS`, otherwise the call reverts with `CurveLib/invalid-deposit-amounts`.

`require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");

        ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        require(
            params.depositAmounts.length == curvePool.N_COINS(),
            "CurveLib/invalid-deposit-amounts"
        );`
