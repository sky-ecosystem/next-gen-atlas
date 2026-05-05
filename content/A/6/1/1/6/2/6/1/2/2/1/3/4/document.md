---
id: b0afea3f-9ff2-4462-a771-522b1256a343
docNo: A.6.1.1.6.2.6.1.2.2.1.3.4
name: Get Current Rate Limit
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.3.4 - Get Current Rate Limit [Core]

Anyone can query the current rate limit value for a specific key, accounting for time-based slope accrual. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData for the key from the _data mapping.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max.
- Otherwise, the contract will calculate and return the minimum of (slope * time elapsed since lastUpdated + lastAmount) and maxAmount.

The function call is as follows:

`function getCurrentRateLimit(bytes32 key) public override view returns (uint256)`
