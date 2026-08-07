---
id: 315b3614-18bb-4ca0-b1c7-3459fd449ad8
docNo: A.2.2.10.1.1.1.5.2.5.2.3
name: Remove Liquidity From Uniswap v3 Position
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.2.3 - Remove Liquidity From Uniswap v3 Position [Core]

The Uniswap v3 Facet's `removeLiquidity` function first confirms the ALM Proxy is the current owner of the position, then decreases the specified amount of liquidity from it. It does this by calling the Uniswap v3 position manager's `decreaseLiquidity` function. Before the decrease, the facet collects any fees the position has already accrued. The `decreaseLiquidity` call itself does not transfer any tokens to the ALM Proxy; it only credits the withdrawn amounts to the position as tokens owed. After the decrease, the facet collects again, and this second collection is what delivers the withdrawn principal to the ALM Proxy. The withdrawal does not complete unless the resulting amounts satisfy the specified minimums, and those minimums must in turn satisfy the configured maximum slippage for the pool. Unlike the deposit-side check on adding liquidity, this check is against the amounts actually withdrawn, measured after the decrease and both collections have already executed; it is not checked against an independent price reference computed before execution.
