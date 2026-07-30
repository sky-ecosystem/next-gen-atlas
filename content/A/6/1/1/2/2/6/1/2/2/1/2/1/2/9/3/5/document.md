---
id: 3b093990-0f1e-47d5-bbc2-ab49385e8383
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.5
name: Collect Tokens
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.5 - Collect Tokens [Core]

The operator must collect the withdrawn tokens by calling `collect` on the `positionManager` through the `proxy`, receiving `amount0Collected` and `amount1Collected`, then record the `proxy` ending balances of `token0` and `token1`.

`(amount0Collected, amount1Collected) = _collectAll(
            context.proxy,
            address(params.positionManager),
            params.tokenId,
            address(context.proxy)
        );

        uint256 amount0CollectedAfter = IERC20(token0).balanceOf(address(context.proxy));
        uint256 amount1CollectedAfter = IERC20(token1).balanceOf(address(context.proxy));`
