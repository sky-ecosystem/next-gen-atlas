---
id: fd4778b5-78e7-49fc-a785-c2dfed2e5246
docNo: A.6.1.1.2.2.6.1.3.1.7.7.4.1
name: Max Exchange Rate
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.7.7.4.1 - Max Exchange Rate [Core]

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 3 RLUSD:

- `setMaxExchangeRate(SENTORA_RLUSD_MAIN_V2, 1e18, 3e18)`
