---
id: 26eec581-240e-4214-85a4-ee9309b986d4
docNo: A.2.2.10.1.1.1.5.2.3.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.3.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate an Aave market deposit. The call is made to the Diamond PAU Controller, which dispatches it to the Aave Facet to perform the deposit on behalf of the ALM Proxy.
