---
id: b559e279-2bf0-4047-8e23-023c1eaf1928
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.3
name: Compute Price Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.3 - Compute Price Limit [Core]

The operator must confirm `tokenIn` is one of the pool's two tokens, consult the pool's TWAP tick, and compute the `sqrtPriceLimitX96` bound from the TWAP tick offset by `tickDelta` and bounded to the `TickMath` minimum and maximum, so the swap cannot move the price beyond the configured limit.

`SwapCache memory cache = _populateSwapCache(context, params);`
