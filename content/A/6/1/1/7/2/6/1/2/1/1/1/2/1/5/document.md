---
id: 0eed3609-62a2-4c5b-ae5b-4f78212252ee
docNo: A.6.1.1.7.2.6.1.2.1.1.1.2.1.5
name: AdministeredAgent Contract
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.5 - AdministeredAgent Contract [Core]

The address of the AdministeredAgent contract is: `0x1837505D104F7a6D8b7e19452610B0A3D652EF12`. The AdministeredAgent holds the Allocator Role as specified in [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) and mediates relayer access to the Controller: the Relayer Multisigs are registered as its Actors, as specified in [A.2.2.10.1.1.1.3.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55), and submit operations through it, while the Freezer Multisig is registered as a Revoker, as specified in [A.2.2.10.1.1.1.3.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e), authorized to remove a compromised Actor.
