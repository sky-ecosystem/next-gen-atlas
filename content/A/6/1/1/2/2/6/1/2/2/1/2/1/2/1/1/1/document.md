---
id: 044fed6d-5a18-48d1-89df-777f86e4652a
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `mintUSDS`, enforced by the `onlyRole(RELAYER)` gate on the function; there is no other precondition or active-state check.

`function mintUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)`
