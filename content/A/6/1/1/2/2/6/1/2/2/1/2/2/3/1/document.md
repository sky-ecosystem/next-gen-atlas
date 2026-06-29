---
id: 24c508b8-50b2-4a28-8f17-6a78ae479672
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.3.1
name: Allocator Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.3.1 - Allocator Role [Core]

Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS mint. The call is made to the Diamond PAU Controller, which dispatches it to the USDS Facet to perform the mint on behalf of the ALM Proxy.
