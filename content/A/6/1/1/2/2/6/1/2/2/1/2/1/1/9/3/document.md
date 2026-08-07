---
id: a6b7dd4b-6935-4d69-8af7-34d34734b455
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.3
name: Set And Emit Max Exchange Rate
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.3 - Set And Emit Max Exchange Rate [Core]

The operator must set the maximum exchange rate for the `token` to the value computed by `_getExchangeRate` from the provided `shares` and `maxExpectedAssets`, which returns `1e36 * assets / shares` at `1e36` precision and reverts with `MainnetController/zero-shares` when `shares` is zero while assets are non-zero. This value is written to the `maxExchangeRates` mapping for the `token` and emitted through the `MaxExchangeRateSet` event to the blockchain logs.

`        emit MaxExchangeRateSet(
            token,
            maxExchangeRates[token] = _getExchangeRate(shares, maxExpectedAssets)
        );
    }`
