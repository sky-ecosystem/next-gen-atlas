---
id: c5fa2d90-df64-406e-a53d-9694d448b161
docNo: A.6.1.1.2.2.6.1.3.1.7.4.2.4.3
name: Max Exchange Rate
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.7.4.2.4.3 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 4 PYUSD (current share price is 2).

- `setMaxExchangeRate(STEAKHOUSE_PYUSD_MAIN, 1e18, 4e6)`
