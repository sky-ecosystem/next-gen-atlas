---
id: a710528f-e695-4262-bab1-e5ee57241315
docNo: A.6.1.1.3.2.6.1.2.2.1.1.3.5
name: Trigger Rate Limit Decrease
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.3.5 - Trigger Rate Limit Decrease [Core]

Only an operator with the controller role can trigger a decrease in the rate limit for a specific key by a given amount. Calling this function will carry out the following actions:

- The contract will retrieve the Rate LimitData storage for the key from the data mapping.
- The contract will require that maxAmount is greater than 0, reverting with "Rate Limits/zero-maxAmount" if not.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max without changes.
- The contract will calculate the currentRate Limit using getCurrentRate Limit.
- The contract will require that amountToDecrease is less than or equal to currentRate Limit, reverting with "Rate Limits/rate-limit-exceeded" if not.
- The contract will update lastAmount to currentRate Limit minus amountToDecrease and set lastUpdated to the current block timestamp.
- The contract will emit a Rate LimitDecreaseTriggered event with the key, amountToDecrease, currentRate Limit, and newLimit.
- The contract will return the newLimit.

The function call is as follows:

`function triggerRate LimitDecrease(bytes32 key, uint256 amountToDecrease) external override onlyRole(CONTROLLER) returns (uint256 newLimit)`
