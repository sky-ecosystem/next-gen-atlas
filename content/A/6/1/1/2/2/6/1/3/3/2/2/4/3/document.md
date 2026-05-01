---
id: 3b96571e-bd04-44dd-b729-3c59288d80b1
docNo: A.6.1.1.2.2.6.1.3.3.2.2.4.3
name: Max Exchange Rate
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.3.2.2.4.3 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 USDC.

- `setMaxExchangeRate(STEAKHOUSE_PRIME_INSTANT_USDC_V2, 1e18, 2e6)`
