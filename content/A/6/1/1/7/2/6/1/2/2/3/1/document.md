---
id: 39b320a8-240c-487d-9c72-25b8a2457a4b
docNo: A.6.1.1.7.2.6.1.2.2.3.1
name: Remove Compromised Actor As Freezer
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.7.2.6.1.2.2.3.1 - Remove Compromised Actor As Freezer [Core]

In the event of a compromised or malicious Actor, the Freezer Multisig — registered as a Revoker on the AdministeredAgent, as specified in [A.2.2.10.1.1.1.3.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e) — removes that Actor by calling `removeActor` on the AdministeredAgent contract. Removing the Actor prevents it from submitting further operations, while the Allocator Role itself remains with the AdministeredAgent. This action should only be taken if a Relayer Multisig's keys have been leaked or compromised and the Actor is in the control of an external bad actor.
