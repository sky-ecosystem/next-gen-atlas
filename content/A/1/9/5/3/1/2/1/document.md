---
id: e4e3c3d9-939d-43ef-9f7a-64f5d4cfe7d6
docNo: A.1.9.5.3.1.2.1
name: Permissionless Cancellation Of Single Planned Governance Action
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.5.3.1.2.1 - Permissionless Cancellation Of Single Planned Governance Action [Core]

If the Protego contract has authority from Sky Governance, any user can permissionlessly invoke the `drop` function to cancel a specified Spell:

`/// @notice Permissionlessly drop anything that has been planned on the pause.
drop(address _usr, bytes32 _tag, bytes memory _fax, uint256 _eta)`

The parameters of the `drop` function are defined in [A.1.9.5.3.1.3 - Protego Parameters](55195cdc-90c3-4133-a0e4-792444b60ed8).
