---
id: 499b7fbe-d555-4d5d-8025-4611ed308d9b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.3
name: Verify Ownership And Snapshot Balances
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.3 - Verify Ownership And Snapshot Balances [Core]

The operator must ensure the `proxy` owns the position `tokenId`, then record the `proxy` starting balances of `token0` and `token1` before the withdrawal.

`require(params.positionManager.ownerOf(params.tokenId) == address(context.proxy), "UniswapV3Lib/proxy-does-not-own-token-id");

        uint256 amount0CollectedBefore = IERC20(token0).balanceOf(address(context.proxy));
        uint256 amount1CollectedBefore = IERC20(token1).balanceOf(address(context.proxy));`
