---
id: f629bb8f-afb2-4bfc-b7fa-3f5fbaa2c2f9
docNo: A.6.1.1.5.2.6.1.2.2.1.3.4
name: Get Current Rate Limit
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.3.4 - Get Current Rate Limit [Core]

Anyone can query the current rate limit value for a specific key, accounting for time-based slope accrual. Calling this function will carry out the following actions:

- The contract will retrieve the Rate LimitData for the key from the _data mapping.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max.
- Otherwise, the contract will calculate and return the minimum of (slope * time elapsed since lastUpdated + lastAmount) and maxAmount.

The function call is as follows:

`function getCurrentRate Limit(bytes32 key) public override view returns (uint256)`
