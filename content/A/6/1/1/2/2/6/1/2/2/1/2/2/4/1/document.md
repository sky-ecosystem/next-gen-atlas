---
id: a9e7e4c1-e9d7-4e72-b66d-f6233fea5e1f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.4.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.4.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS burn. The call is made to the Diamond PAU Controller, which dispatches it to the USDS Facet to perform the burn on behalf of the ALM Proxy.
