---
id: 26eec581-240e-4214-85a4-ee9309b986d4
docNo: A.2.2.10.1.1.1.5.2.3.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.3.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate an Aave market deposit by calling the `aave_deposit` function on the Diamond PAU Controller, passing the address of the aToken and the amount to deposit. The Controller dispatches the call to the Aave Facet, which performs the deposit on behalf of the ALM Proxy.
