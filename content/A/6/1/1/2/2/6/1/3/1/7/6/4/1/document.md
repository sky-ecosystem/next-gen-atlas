---
id: 1f14f407-9eeb-4e6b-bf6e-c837b5560f28
docNo: A.6.1.1.2.2.6.1.3.1.7.6.4.1
name: Max Exchange Rate
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.7.6.4.1 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 3 PYUSD:

- `setMaxExchangeRate(SENTORA_PYUSD_MAIN_V2, 1e18, 3e6)`
