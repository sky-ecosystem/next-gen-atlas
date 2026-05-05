---
id: 6022623f-e7cd-4a04-a8ab-e5b61c11a9da
docNo: A.1.9.5.3.1.2.2
name: Permissionless Cancellation Of Multiple Planned Governance Actions
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.5.3.1.2.2 - Permissionless Cancellation Of Multiple Planned Governance Actions [Core]

If the Protego contract has authority from Sky Governance, any user can permissionlessly invoke the `drop` function to cancel a specified set of Spells:

`/// @notice Drop multiple plans in a single call.
drop(Plan[] calldata plans)`

The parameter of the `drop` function is defined in [A.1.9.5.3.1.3 - Protego Parameters](55195cdc-90c3-4133-a0e4-792444b60ed8).
