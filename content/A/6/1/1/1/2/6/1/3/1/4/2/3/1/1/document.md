---
id: 463dba18-1e74-49bd-b06f-7df0b0cedae7
docNo: A.6.1.1.1.2.6.1.3.1.4.2.3.1.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownAssetsSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownAssetsSUSDe(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`
