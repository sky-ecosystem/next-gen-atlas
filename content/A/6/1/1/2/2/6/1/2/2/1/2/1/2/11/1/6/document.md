---
id: 267a7de0-dd91-4cbc-bbd8-22b8de98067e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.6
name: Verify Amount Received
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.6 - Verify Amount Received [Core]

The operator must compute the amount of `tokenOut` actually received by the `proxy` and ensure it meets the caller's `minAmountOut`. `PendleLib` reverts with `min-amount-not-met` if the received amount is below `minAmountOut`.

`        uint256 totalTokenOutAmount = IERC20(tokenOut).balanceOf(address(params.proxy)) - tokenOutAmountBefore;

        require(totalTokenOutAmount >= params.minAmountOut, "PendleLib/min-amount-not-met");`
