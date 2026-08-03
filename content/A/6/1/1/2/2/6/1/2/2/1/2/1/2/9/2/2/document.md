---
id: c3aab084-e3f1-4e7b-af33-0c1ea9a15d06
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.2
name: Validate Deposit Parameters
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.2 - Validate Deposit Parameters [Core]

The operator must ensure at least one of the target amounts is greater than zero, that `maxSlippage` is set for the pool, and that the pool's `twapSecondsAgo` is set before the deposit is routed through `UniswapV3Lib`.

`function addLiquidity(UniV3Context calldata context, AddLiquidityParams calldata params)
        external
        returns (uint256 tokenId, uint128 liquidity, uint256 amount0, uint256 amount1)
    {
        require(
            params.target.amount0 > 0 || params.target.amount1 > 0,
            "UniswapV3Lib/zero-amount"
        );

        require(params.maxSlippage > 0,     "UniswapV3Lib/max-slippage-not-set");
        require(params.twapSecondsAgo != 0, "UniswapV3Lib/zero-twap-seconds");`
