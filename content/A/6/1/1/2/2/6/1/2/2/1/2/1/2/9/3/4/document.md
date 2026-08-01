---
id: 93a4feb6-687b-44a4-b5c8-5ac466a356eb
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.4
name: Decrease Liquidity
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.4 - Decrease Liquidity [Core]

The operator must decrease the position's liquidity by calling `decreaseLiquidity` on the `positionManager` through the `proxy`, passing the requested `liquidity`, the minimum amounts, and the `deadline`.

`_decreaseLiquidityCall(
            context.proxy,
            address(params.positionManager),
            params.tokenId,
            params.liquidity,
            params.min,
            params.deadline
        );`
