---
id: b0e0d442-ee24-4916-8c95-fe96ff066808
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDSToDAI`.

`function swapUSDSToDAI(uint256 usdsAmount)
        external
        onlyRole(RELAYER)`
