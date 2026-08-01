---
id: 381cbdf4-6778-421c-8565-b8de2e8672ba
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.6
name: Enforce Exchange Rate
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.6 - Enforce Exchange Rate [Core]

The operator must ensure the realized exchange rate of the deposit does not exceed the configured `maxExchangeRates` for the `token`, otherwise the call reverts with `MainnetController/exchange-rate-too-high`. The exchange rate is computed by `_getExchangeRate(shares, amount)` as `EXCHANGE_RATE_PRECISION * amount / shares` at `1e36` precision, guarding against depositing into a vault whose shares are priced above the acceptable threshold.

`        require(
            _getExchangeRate(shares, amount) <= maxExchangeRates[token],
            "MainnetController/exchange-rate-too-high"
        );`
