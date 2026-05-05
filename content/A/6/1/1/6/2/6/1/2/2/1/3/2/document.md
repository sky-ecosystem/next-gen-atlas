---
id: 89b060bd-1026-46ec-ab32-d032edb58f83
docNo: A.6.1.1.6.2.6.1.2.2.1.3.2
name: Set Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.3.2 - Set Rate Limit Data [Core]

Only an operator with the admin role is able to set or update rate limit data for a specific key, including maxAmount, slope, and historical values. There are two overloads for flexibility. Calling these functions will carry out the following actions:

- The contract will require that lastAmount is less than or equal to maxAmount, reverting with "RateLimits/invalid-lastAmount" if not.
- The contract will require that lastUpdated is less than or equal to the current block timestamp, reverting with "RateLimits/invalid-lastUpdated" if not.
- The contract will store the provided data in the _data mapping as a RateLimitData struct.
- The contract will emit a RateLimitDataSet event with the key and provided values.

The function calls are as follows:

`function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope, uint256 lastAmount, uint256 lastUpdated) public override onlyRole(DEFAULT_ADMIN_ROLE)

function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override`
