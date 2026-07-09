---
id: 1bcd7223-f506-4a1e-8897-574d942de1a3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.5.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.5.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS to USDC swap. The call is made to the Diamond PAU Controller, which dispatches it to the PSM Facet to perform the swap on behalf of the ALM Proxy.
