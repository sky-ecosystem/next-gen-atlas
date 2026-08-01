---
id: 5ddf7a99-ba35-4fc0-984a-1fa59e697695
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.5
name: Execute The Swap
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.5 - Execute The Swap [Core]

The operator must execute the swap by calling `exactInputSingle` on the `router` through the `proxy`, receiving `amountOut` of the output token, then record the `proxy` ending balance of `tokenIn`.

`amountOut               = _callSwap(context, params, cache);
        uint256 endingBalance   = IERC20(params.tokenIn).balanceOf(address(context.proxy));`
