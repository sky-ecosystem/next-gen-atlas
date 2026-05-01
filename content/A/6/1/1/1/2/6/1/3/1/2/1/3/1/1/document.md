---
id: 25fd8f89-cb76-464e-b659-e2e1885ac4c5
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositAave`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function depositAave(address aToken, uint256 amount)
external
onlyRole(RELAYER)
isActive`
