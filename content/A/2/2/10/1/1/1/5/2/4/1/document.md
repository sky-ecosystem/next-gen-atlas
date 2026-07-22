---
id: c5a30d6c-6f3a-48a1-af35-39c0ee0bece4
docNo: A.2.2.10.1.1.1.5.2.4.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.4.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate an Aave market withdrawal. The call is made to the Diamond PAU Controller, which dispatches it to the Aave Facet to perform the withdrawal on behalf of the ALM Proxy.
