---
id: 23d1b504-bd08-4759-b2d6-9067fdbcaedd
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `burnUSDS`. They must also ensure the contract `isActive` i.e. can process the request.

`function burnUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)
        isActive`
