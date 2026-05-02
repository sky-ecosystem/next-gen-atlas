---
id: bb5f7a55-8c79-4678-a281-8264eb5de225
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.2.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `setDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function setDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`
