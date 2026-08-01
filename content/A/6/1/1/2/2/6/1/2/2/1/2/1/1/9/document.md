---
id: 662ec211-4b25-43db-aca4-48acb08090ec
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.9
name: Set The Max Exchange Rate
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9 - Set The Max Exchange Rate [Core]

The documents herein define the process to set the maximum expected exchange rate for a specific `token`. This value is stored in the `maxExchangeRates` mapping with `1e36` precision and caps the exchange rate accepted when depositing into the `token` through `depositERC4626`, reverting with `MainnetController/exchange-rate-too-high` when the realized rate exceeds it.
