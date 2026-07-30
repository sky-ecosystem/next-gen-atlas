---
id: 3970df59-0e49-415c-ac0f-504f92d533f8
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.2
name: Validate Market Expiry And Minimum Output
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.2 - Validate Market Expiry And Minimum Output [Core]

The operator must ensure the Pendle market has reached expiry and that a non-zero `minAmountOut` was provided. `PendleLib` reverts with `market-not-expired` if `pendleMarket.isExpired()` is false, and with `min-amount-out-not-set` if `minAmountOut` is zero.

`{
        require(params.pendleMarket.isExpired(), "PendleLib/market-not-expired");
        require(params.minAmountOut != 0,        "PendleLib/min-amount-out-not-set");`
