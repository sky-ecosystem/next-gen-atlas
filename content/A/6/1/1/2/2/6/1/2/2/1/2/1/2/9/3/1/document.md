---
id: 1eb0e395-bd23-4088-ab1c-8971f2acbb17
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeLiquidityUniswapV3`. The function decreases a liquidity position and collects the withdrawn tokens to the `proxy`.

`function removeLiquidityUniswapV3(
        address                   pool,
        uint256                   tokenId,
        uint128                   liquidity,
        UniswapV3Lib.TokenAmounts calldata min,
        uint256                   deadline
    )
        external
        onlyRole(RELAYER)
        returns (uint256 amount0Collected, uint256 amount1Collected)`
