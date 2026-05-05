---
id: 37aed332-50c8-4392-91be-095bd13139d1
docNo: A.6.1.1.5.2.6.1.2.2.1.3.3
name: Set Unlimited Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.3.3 - Set Unlimited Rate Limit Data [Core]

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRate LimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRate LimitData(bytes32 key) external override`
