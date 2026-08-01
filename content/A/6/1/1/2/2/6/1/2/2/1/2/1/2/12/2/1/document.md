---
id: 4c6fb82f-4c19-453a-a91c-f96a5979c39c
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapDAIToUSDS`.

`function swapDAIToUSDS(uint256 daiAmount)
        external
        onlyRole(RELAYER)`
