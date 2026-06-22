---
id: c34e9845-e412-4646-8069-48c3cc1914e5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.2.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.2.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a Basin withdrawal. The call is made to the Diamond PAU Controller, which dispatches it to the Basin Facet to perform the withdrawal on behalf of the ALM Proxy.
