---
id: 0639862b-3640-48d1-9117-b713d8ba89b7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.3
name: Approve The Position Manager
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.3 - Approve The Position Manager [Core]

The operator must read `token0` and `token1` from the pool and approve the `positionManager` to spend the target amount of each token on behalf of the `proxy`.

`IUniswapV3PoolLike pool = IUniswapV3PoolLike(context.pool);

        address token0 = pool.token0();
        address token1 = pool.token1();

        ERC20Lib.approve(context.proxy, token0, address(params.positionManager), params.target.amount0);
        ERC20Lib.approve(context.proxy, token1, address(params.positionManager), params.target.amount1);`
