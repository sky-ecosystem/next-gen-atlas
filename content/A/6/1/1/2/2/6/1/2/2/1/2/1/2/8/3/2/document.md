---
id: ce61aae1-480f-4e87-855d-c2dab99ede1c
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.2
name: Validate Minimum Withdraw Amounts
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.2 - Validate Minimum Withdraw Amounts [Core]

The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`. They must also ensure the length of `minWithdrawAmounts` matches the pool's `N_COINS`, otherwise the call reverts with `CurveLib/invalid-min-withdraw-amounts`.

`require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");

        ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        require(
            params.minWithdrawAmounts.length == curvePool.N_COINS(),
            "CurveLib/invalid-min-withdraw-amounts"
        );`
