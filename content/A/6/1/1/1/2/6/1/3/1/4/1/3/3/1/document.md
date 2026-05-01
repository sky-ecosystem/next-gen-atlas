---
id: 157361f8-7758-4e6b-a04d-a592d40b3b41
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.3.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function removeDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`
