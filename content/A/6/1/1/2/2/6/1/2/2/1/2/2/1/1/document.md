---
id: 255ff22b-80c5-4a1c-946c-d5bf64e098f0
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.1.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.1.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a Basin deposit. The call is made to the Diamond PAU Controller, which dispatches it to the Basin Facet to perform the deposit on behalf of the ALM Proxy.
