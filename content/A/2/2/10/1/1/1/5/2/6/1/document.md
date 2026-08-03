---
id: 75edeae6-46e4-4761-b2c7-0416038c97cf
docNo: A.2.2.10.1.1.1.5.2.6.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.6.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a Basin withdrawal by calling the `basin_withdraw` function on the Diamond PAU Controller, passing the address of the Basin contract, the address of the asset, the maximum amount to withdraw, and the minimum conversion rate (`minConversionRate`). The Controller dispatches the call to the Basin Facet, which performs the withdrawal on behalf of the ALM Proxy.
