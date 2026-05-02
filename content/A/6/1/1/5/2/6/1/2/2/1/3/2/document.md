---
id: 993bbc35-1692-4c1b-87b2-de5997e90bf5
docNo: A.6.1.1.5.2.6.1.2.2.1.3.2
name: Set Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.3.2 - Set Rate Limit Data [Core]

Only an operator with the admin role is able to set or update rate limit data for a specific key, including maxAmount, slope, and historical values. There are two overloads for flexibility. Calling these functions will carry out the following actions:

- The contract will require that lastAmount is less than or equal to maxAmount, reverting with "Rate Limits/invalid-lastAmount" if not.
- The contract will require that lastUpdated is less than or equal to the current block timestamp, reverting with "Rate Limits/invalid-lastUpdated" if not.
- The contract will store the provided data in the _data mapping as a Rate LimitData struct.
- The contract will emit a Rate LimitDataSet event with the key and provided values.

The function calls are as follows:

`function setRate LimitData(bytes32 key, uint256 maxAmount, uint256 slope, uint256 lastAmount, uint256 lastUpdated) public override onlyRole(DEFAULT_ADMIN_ROLE)

function setRate LimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override`
