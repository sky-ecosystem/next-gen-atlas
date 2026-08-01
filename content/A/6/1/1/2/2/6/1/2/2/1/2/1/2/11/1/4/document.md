---
id: df5d543b-00e3-4c7c-bd85-4c766025ee32
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.4
name: Approve Router Spend And Snapshot Balance
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.4 - Approve Router Spend And Snapshot Balance [Core]

The operator must approve the `PENDLE_ROUTER` to spend `pyAmountIn` of the `PT` token on behalf of the `proxy`, then record the `proxy`'s `tokenOut` balance before the redemption so the amount received can be measured afterwards.

`        ERC20Lib.approve(params.proxy, pt, params.pendleRouter, params.pyAmountIn);

        uint256 tokenOutAmountBefore = IERC20(tokenOut).balanceOf(address(params.proxy));`
