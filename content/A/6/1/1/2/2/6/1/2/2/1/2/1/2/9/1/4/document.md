---
id: e6362ec9-4c75-49d3-9706-fec84f814126
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.4
name: Approve The Router
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.4 - Approve The Router [Core]

The operator must approve the Uniswap V3 `router` to spend `amountIn` of `tokenIn` on behalf of the `proxy`, then record the `proxy` starting balance of `tokenIn`.

`ERC20Lib.approve(context.proxy, params.tokenIn, address(params.router), params.amountIn);

        uint256 startingBalance = IERC20(params.tokenIn).balanceOf(address(context.proxy));`
