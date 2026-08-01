---
id: c03bfbe1-1712-44a8-87a7-68a3fc720f66
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.5
name: Mint Or Increase Liquidity
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.5 - Mint Or Increase Liquidity [Core]

The operator must, when `tokenId` is zero, mint a new position after checking the requested `tick` range is within the governance-set bounds and aligned to the pool's tick spacing; otherwise the operator must increase liquidity on the existing position owned by the `proxy`.

`if (params.tokenId == 0) {
            (tokenId, liquidity, amount0, amount1) = _mintLiquidity(context, params);
        } else {
            (tokenId, liquidity, amount0, amount1) = _addLiquidityToExistingPosition(context, params);
        }`
