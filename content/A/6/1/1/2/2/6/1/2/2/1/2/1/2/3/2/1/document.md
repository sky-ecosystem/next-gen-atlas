---
id: a3637c8d-ce3e-4cc8-ae15-2a8623a841db
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDCToUSDS`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function swapUSDCToUSDS(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`
