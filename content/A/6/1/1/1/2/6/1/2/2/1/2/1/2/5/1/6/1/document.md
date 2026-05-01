---
id: b25fcca3-374b-408d-9715-bb514ee209b1
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.1
name: Check CCTP Transfer Limit
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.1 - Check CCTP Transfer Limit [Core]

The operator must check the `transfer limit`. They must retrieve the maximum amount of USDC that can be transferred in a single CCTP message. This limit is fetched from the `localMinter` contract associated with CCTP.

`uint256 burnLimit = cctp.localMinter().burnLimitsPerMessage(address(usdc));`
