---
id: aae0e1ba-4ed0-4484-9187-3e53f3695ae8
docNo: A.6.1.1.7.2.6.1.2.2.1.1
name: Role Hierarchies And Permissions
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.7.2.6.1.2.2.1.1 - Role Hierarchies And Permissions [Core]

The roles and permissions of the Diamond PAU Instance are the Liquidity Layer roles defined in [A.2.2.10.1.1.1.3 - Liquidity Layer Role Definitions](2ae4b91a-6900-41e8-9718-32805b956550), managed by the AccessControls contract. For the Osero Liquidity Layer, the `DEFAULT_ADMIN_ROLE` is held by the Osero SubProxy, and the `CONTROLLER` role by the Controller contract. The `ALLOCATOR_ROLE` is held by the AdministeredAgent contract, as specified in [A.6.1.1.7.2.6.1.2.1.1.1.2.1.5 - AdministeredAgent Contract](0eed3609-62a2-4c5b-ae5b-4f78212252ee). The Osero Relayer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.1 - Osero Relayer Multisig](1830fb80-a44b-4aaf-b72c-7c4997cb9486)) and the Core Operator Relayer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.2 - Core Operator Relayer Multisig](f48b14c7-6dd1-4d10-b546-a604be45758c)) are registered as its Actors, as specified in [A.2.2.10.1.1.1.3.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55). The Freezer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.3 - Freezer Multisig](51460bc2-f5fb-4302-912a-ed3e6943aae0)) is registered as a Revoker, as specified in [A.2.2.10.1.1.1.3.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e).
