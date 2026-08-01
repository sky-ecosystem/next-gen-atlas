---
id: 8eea7011-c299-4861-bf2e-0adb78e3ef30
docNo: A.2.2.10.1.1.1.5.2.1.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.1.1 - Allocator Role [Core]

Only an address holding the [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDS mint by calling the `usds_mint` function on the Diamond PAU Controller, passing the amount of USDS to mint. The Controller dispatches the call to the USDS Facet, which performs the mint on behalf of the ALM Proxy.
