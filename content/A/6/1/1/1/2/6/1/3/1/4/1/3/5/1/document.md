---
id: 083618d3-6102-4a1a-bc7a-dfa854d49197
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.5.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeBurn`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeBurn(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`
