---
id: 7c4bdc16-13e0-47b4-8988-18e9720eb292
docNo: A.6.1.1.6.2.6.1.2.2.1.3.3
name: Set Unlimited Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.3.3 - Set Unlimited Rate Limit Data [Core]

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRateLimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRateLimitData(bytes32 key) external override`
