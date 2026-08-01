---
id: 8356f5f0-758d-4c7f-b649-b21243d5d346
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.3
name: Check Max Slippage
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.3 - Check Max Slippage [Core]

The operator must ensure a maximum slippage has been configured for the `aToken`. The transaction reverts with `max-slippage-not-set` when `maxSlippages[aToken]` is zero.

`        require(maxSlippages[aToken] != 0, "MainnetController/max-slippage-not-set");`
