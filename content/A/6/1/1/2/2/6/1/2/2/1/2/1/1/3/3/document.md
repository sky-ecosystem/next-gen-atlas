---
id: e55c742b-8aed-4afd-aab9-ae9dc0bdc007
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.3
name: Set Max Slippage For Pool
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.3 - Set Max Slippage For Pool [Core]

The operator must record the `maxSlippage` for the given `pool` in the `maxSlippages` mapping, which is stored with `1e18` precision.

`        maxSlippages[pool] = maxSlippage;`
