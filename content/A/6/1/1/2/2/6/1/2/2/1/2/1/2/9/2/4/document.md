---
id: d48bbd5d-da24-472f-83cc-20d817e13487
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.4
name: Validate Minimum Amounts
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.4 - Validate Minimum Amounts [Core]

The operator must validate the minimum amounts by consulting the TWAP tick, computing the expected token amounts for the target liquidity, and requiring each `min` amount to be at least the expected amount scaled by `maxSlippage`.

`_validateAddLiquidityMinAmounts(context, params);`
