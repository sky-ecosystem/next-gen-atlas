---
id: 0a5ccc61-eaf4-4b49-80d7-770e29178c1a
docNo: A.6.1.1.3.2.6.1.2.2.1.1.3.3
name: Set Unlimited Rate Limit Data
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.3.3 - Set Unlimited Rate Limit Data [Core]

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRate LimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRate LimitData(bytes32 key) external override`
