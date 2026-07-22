---
id: 53d3749c-ef45-45ed-9657-373580abe3cf
docNo: A.2.2.10.1.1.1.5.2.2.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.2.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS burn. The call is made to the Diamond PAU Controller, which dispatches it to the USDS Facet to perform the burn on behalf of the ALM Proxy.
