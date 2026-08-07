---
id: 6cfcbc24-2d8d-40fe-bc90-ec679c084ef0
docNo: A.2.2.10.1.1.1.5.2.5.2.1
name: Allocator Role
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.2.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may remove liquidity by calling the `uniswapV3_removeLiquidity` function on the Diamond PAU Controller. The call passes the address of the pool, the identifier of the position, the amount of liquidity to remove, the minimum amounts of each pool token to accept, and a deadline. The Controller dispatches the call to the Uniswap v3 Facet, which performs the withdrawal on behalf of the ALM Proxy.
