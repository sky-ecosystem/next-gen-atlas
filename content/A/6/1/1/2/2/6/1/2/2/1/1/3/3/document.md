---
id: 6d6622aa-5d56-48e0-b8e9-1addd309fc9b
docNo: A.6.1.1.2.2.6.1.2.2.1.1.3.3
name: Allocator Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.3.3 - Allocator Role [Core]

The `ALLOCATOR_ROLE` is authorized to call functions on the Controller contract to perform operations on behalf of the ALM Proxy contract. The Allocator Role is held by the AdministeredAgent contract, as specified in [A.6.1.1.2.2.6.1.2.1.1.1.4.1.5 - AdministeredAgent Contract](d58e14aa-0901-4aa9-af44-6281161be162), which mediates access for the Grove Liquidity Layer relayer system. The same relayer multisigs used by the monolithic ALM Controller, whose addresses are specified in [A.6.1.1.2.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig Addresses](51b50a8f-eb29-4424-bb0a-8247d2acce7d), are registered as actors of the AdministeredAgent and submit operations through it. An actor may be removed from the AdministeredAgent by any address holding the Freezer Role, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3.4 - Freezer Role](d910ae36-1251-4385-b989-f303878ed094).
