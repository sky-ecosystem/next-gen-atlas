---
id: eacdbe29-1c6b-43b4-93a6-5e4eb9aa0fa7
docNo: A.6.1.1.1.2.6.1.3.1.4.2.3.2.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownSharesSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownSharesSUSDe(uint256 susdeAmount)
        external
        onlyRole(RELAYER)
        isActive`
