---
id: e9ed6ba5-c7a8-4400-acd4-abe0e3f75fb3
docNo: A.6.1.1.2.2.6.1.3.7.1.1.2.4.3
name: Max Exchange Rate
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.7.1.1.2.4.3 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 1.15 USDG (current share price is ~1.00).

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_USDG_V2, 1e18, 1.15e6)`
