---
id: 3986fe17-e84d-407a-9192-61e6b842426a
docNo: A.2.2.10.1.1.1.2.5.2.5.3.3
name: Swap Tokens Through Uniswap v3 Pool
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.2.5.2.5.3.3 - Swap Tokens Through Uniswap v3 Pool [Core]

The Uniswap v3 Facet's `swap` function attempts to sell the specified amount of the given token through the Uniswap v3 router for the pool's other token. The execution price is bounded against the pool's time-weighted average price by the specified maximum tick deviation. If the swap reaches this price limit before selling the full specified amount, execution stops without reverting, and part of the specified amount goes unsold. The Uniswap v3 Facet measures the amount actually sold by comparing the ALM Proxy's balance of the given token before and after the swap, and applies the Rate Limit against that measured amount rather than the specified amount. The swap does not complete unless the specified tick deviation falls within the configured maximum for the pool and the amount received is at least the specified minimum, which must be a non-zero value. The maximum tick deviation is the only governance-configured control on the swap's execution quality; the minimum amount received has no equivalent governance floor beyond being non-zero.
