---
id: 20f412f9-ed6b-4579-bd0c-550f492b4bb7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.3
name: Get Claimable Shares
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.3 - Get Claimable Shares [Core]

The operator must determine the number of `shares` that can be claimed by calling `maxMint` for the `proxy` on the ERC-7540 vault. This is the maximum amount of shares the fulfilled deposit request entitles the `proxy` to mint.

`        uint256 shares = IERC7540(token).maxMint(address(proxy));`
