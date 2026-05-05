---
id: 6894aa1a-4e6d-4372-a989-34258aeddf00
docNo: A.6.1.1.2.2.6.1.3.1.7.3.2.4.3
name: Max Exchange Rate
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.7.3.2.4.3 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 USDC.

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_USDC_V2, 1e18, 2e6)`
