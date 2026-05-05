---
id: a0424398-100e-4c6e-9691-f59efbda6fcd
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `Relayer`. Only the `RELAYER` role is allowed to `mintUSDS`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function mintUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)
        isActive`
