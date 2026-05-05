---
id: bd3ff49e-77af-4757-984d-f8e91346e702
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDSToUSDC`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function swapUSDSToUSDC(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`
