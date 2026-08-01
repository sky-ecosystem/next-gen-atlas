---
id: b2e3b84d-acbd-4704-b55e-e2026aa63058
docNo: A.2.2.10.1.1.1.5.2.5.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.5.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a Basin deposit by calling the `basin_deposit` function on the Diamond PAU Controller, passing the address of the Basin contract, the address of the asset, the amount to deposit, and the minimum number of shares to receive (`minSharesOut`). The Controller dispatches the call to the Basin Facet, which performs the deposit on behalf of the ALM Proxy.
