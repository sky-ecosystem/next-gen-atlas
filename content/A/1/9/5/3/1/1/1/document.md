---
id: 583c1a98-b63a-42fa-b29e-ce0688dcdaf6
docNo: A.1.9.5.3.1.1.1
name: Deployment Of Emergency Drop Spells
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.5.3.1.1.1 - Deployment Of Emergency Drop Spells [Core]

Any user can permissionlessly deploy an Emergency Drop Spell by invoking the `deploy` function on the Protego contract with parameters identifying the planned governance action to be canceled:

`deploy(address _usr, bytes32 _tag, bytes memory _fax, uint256 _eta)(address)`

The parameters of the `deploy` function are defined in [A.1.9.5.3.1.3 - Protego Parameters](55195cdc-90c3-4133-a0e4-792444b60ed8).
