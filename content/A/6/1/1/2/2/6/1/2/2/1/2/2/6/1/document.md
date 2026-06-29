---
id: 4f91b44b-59ec-41d2-9e02-b6c107c643ff
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.6.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.6.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDC to USDS swap. The call is made to the Diamond PAU Controller, which dispatches it to the PSM Facet to perform the swap on behalf of the ALM Proxy.
