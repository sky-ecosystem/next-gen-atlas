---
id: 9984b00e-ecc2-4328-9e86-c0c2e913f79a
docNo: A.6.1.1.1.2.6.1.3.1.4.2.3.3.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.2.3.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function unstakeSUSDe()
        external
        onlyRole(RELAYER)
        isActive`
