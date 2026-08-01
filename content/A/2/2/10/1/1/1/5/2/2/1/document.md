---
id: 53d3749c-ef45-45ed-9657-373580abe3cf
docNo: A.2.2.10.1.1.1.5.2.2.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.2.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDS burn by calling the `usds_burn` function on the Diamond PAU Controller, passing the amount of USDS to burn. The Controller dispatches the call to the USDS Facet, which performs the burn on behalf of the ALM Proxy.
