---
id: 164268cf-b6e5-4c1a-83e5-d199f453cc1b
docNo: A.2.2.10.1.1.1.5.2.5.1.3
name: Add Liquidity To Uniswap v3 Position
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.1.3 - Add Liquidity To Uniswap v3 Position [Core]

The Uniswap v3 Facet's `addLiquidity` function attempts to deposit the target amounts of the pool's two (2) tokens on behalf of the ALM Proxy. To open a new position, it calls the Uniswap v3 position manager's `mint` function. To add to an existing position, it calls the position manager's `increaseLiquidity` function instead — but only after confirming the ALM Proxy is the current owner of that position. Depositing into a tick range does not necessarily use the full target amount of both tokens; the Uniswap v3 Facet measures the amounts actually deposited by comparing the ALM Proxy's token balances before and after the call, rather than relying on the target amounts or the position manager's own return values. The deposit does not complete unless the tick bounds fall within the configured bounds for the pool. Before depositing, the Uniswap v3 Facet checks the specified minimums against expected amounts derived from the pool's time-weighted average price, not its current spot price. Those minimums must in turn satisfy the configured maximum slippage for the pool, and the deposit does not complete unless this check passes.
