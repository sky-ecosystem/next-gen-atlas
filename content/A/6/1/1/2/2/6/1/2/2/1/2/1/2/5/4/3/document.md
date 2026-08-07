---
id: b86ea1fb-a897-41b5-8483-d3473c5e5f32
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.3
name: Get Claimable Assets
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.3 - Get Claimable Assets [Core]

The operator must determine the amount of `assets` that can be claimed by calling `maxWithdraw` for the `proxy` on the ERC-7540 vault. This is the maximum amount of the underlying asset the fulfilled redeem request entitles the `proxy` to withdraw.

`        uint256 assets = IERC7540(token).maxWithdraw(address(proxy));`
