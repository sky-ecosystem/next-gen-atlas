---
id: 85a2ac37-da60-4a04-96eb-600f635ab388
docNo: A.2.2.10.1.1.1.5.2.8.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.8.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDC to USDS swap by calling the `psm_swapUSDCToUSDS` function on the Diamond PAU Controller, passing the amount of USDC to swap. The Controller dispatches the call to the PSM Facet, which performs the swap on behalf of the ALM Proxy.
