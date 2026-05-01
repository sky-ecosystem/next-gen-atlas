---
id: c7a016f1-0d8d-47ad-b91e-39d1a285b149
docNo: A.6.1.1.2.2.6.1.3.1.7.5.4.1
name: Max Exchange Rate
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.7.5.4.1 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 AUSD:

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_AUSD_V2, 1e18, 2e6)`
