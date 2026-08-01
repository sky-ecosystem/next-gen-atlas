---
id: 228b1526-0ddb-48ae-ae8b-cbe3bea71685
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.2
name: Validate Swap Parameters
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.2 - Validate Swap Parameters [Core]

The operator must ensure the requested `tickDelta` does not exceed the pool's configured `swapMaxTickDelta`, that the pool's `twapSecondsAgo` is set, and that `minAmountOut` is greater than zero before the swap is routed through `UniswapV3Lib`.

`function swap(UniV3Context calldata context, SwapParams calldata params) external returns (uint256 amountOut) {
        require(params.tickDelta <= params.poolParams.swapMaxTickDelta, "UniswapV3Lib/invalid-max-tick-delta");
        require(params.poolParams.twapSecondsAgo != 0,                  "UniswapV3Lib/zero-twap-seconds");
        require(params.minAmountOut > 0,                                "UniswapV3Lib/min-amount-not-set");`
