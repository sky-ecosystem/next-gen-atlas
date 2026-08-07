---
id: 9b0217c7-8617-42c3-9e2e-b0b377607f50
docNo: A.2.2.10.1.1.1.5.2.5.3.1
name: Allocator Role
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.3.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a swap by calling the `uniswapV3_swap` function on the Diamond PAU Controller. The call passes the address of the pool, the address of the token to sell, the amount to sell, the minimum amount to receive, and the maximum allowed tick deviation from the pool's time-weighted average price. The Controller dispatches the call to the Uniswap v3 Facet, which performs the swap on behalf of the ALM Proxy.
