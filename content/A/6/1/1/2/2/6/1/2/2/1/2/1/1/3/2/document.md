---
id: a3ff9791-9ea0-49ed-a311-72a5868ea4a3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.2
name: Validate Max Slippage Bound
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.2 - Validate Max Slippage Bound [Core]

The operator must ensure the provided `maxSlippage` does not exceed `1e18`, reverting with `MainnetController/max-slippage-out-of-bounds` otherwise. The `maxSlippage` value is expressed with `1e18` precision.

`{
        require(maxSlippage <= 1e18, "MainnetController/max-slippage-out-of-bounds");`
