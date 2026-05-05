---
id: 9daa0cad-61ef-43e3-9e78-aaddde2e5c35
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawAave` tokens. Also, they ensure the contract `isActive` i.e. can process the request.

`function withdrawAave(address aToken, uint256 amount)
external
onlyRole(RELAYER)
isActive`
