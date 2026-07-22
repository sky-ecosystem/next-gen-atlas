---
id: 8eea7011-c299-4861-bf2e-0adb78e3ef30
docNo: A.2.2.10.1.1.1.5.2.1.1
name: Allocator Role
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.1.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS mint. The call is made to the Diamond PAU Controller, which dispatches it to the USDS Facet to perform the mint on behalf of the ALM Proxy.
