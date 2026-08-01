---
id: d58e14aa-0901-4aa9-af44-6281161be162
docNo: A.6.1.1.2.2.6.1.2.1.1.1.4.1.5
name: AdministeredAgent Contract
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.5 - AdministeredAgent Contract [Core]

The address of the AdministeredAgent contract is: `0xdBD17832df0e57b1732cE1C84c652E820e549BAa`. The AdministeredAgent holds the Allocator Role of the Diamond PAU and mediates relayer access to the Controller: the relayer multisigs are registered as its actors and submit operations through it, while the Freezer Multisig is registered as a revoker authorized to remove a compromised actor, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3 - Diamond PAU Role Hierarchy And Permissions](c4149166-7e65-48d3-81f9-177a4f3f6364).
