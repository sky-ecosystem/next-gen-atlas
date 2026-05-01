---
id: 41214aef-fb81-42d5-ade2-f7263b8fffb0
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.4.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeMint`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeMint(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`
