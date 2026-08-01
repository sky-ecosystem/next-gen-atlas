---
id: 3bd2d8ce-12a5-4519-9e7a-720ef48667ba
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.2
name: Validate Swap Parameters
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.2 - Validate Swap Parameters [Core]

The operator must ensure the `inputIndex` and `outputIndex` differ, otherwise the call reverts with `CurveLib/invalid-indices`. They must also ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`.

`require(params.inputIndex != params.outputIndex, "CurveLib/invalid-indices");

        require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");`
