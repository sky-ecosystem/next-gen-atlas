---
id: 955f7809-40e6-43a3-900d-6992a6e1d2ef
docNo: A.2.2.10.1.1.1.2.5.2.5.1.1
name: Allocator Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.2.5.2.5.1.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may add liquidity by calling the `uniswapV3_addLiquidity` function on the Diamond PAU Controller. The call passes the address of the pool, the identifier of an existing position to increase (or zero to mint a new position), the lower and upper tick bounds, the target amounts of each pool token to deposit, the minimum amounts to accept, and a deadline. The Controller dispatches the call to the Uniswap v3 Facet, which performs the deposit on behalf of the ALM Proxy.
