---
id: 9f76a9bc-5451-4ff7-8dcd-153e4c47fe72
docNo: A.6.1.1.6.2.6.1.2.2.1.3.5
name: Trigger Rate Limit Decrease
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.3.5 - Trigger Rate Limit Decrease [Core]

Only an operator with the controller role can trigger a decrease in the rate limit for a specific key by a given amount. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData storage for the key from the data mapping.
- The contract will require that maxAmount is greater than 0, reverting with "RateLimits/zero-maxAmount" if not.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max without changes.
- The contract will calculate the currentRateLimit using getCurrentRateLimit.
- The contract will require that amountToDecrease is less than or equal to currentRateLimit, reverting with "RateLimits/rate-limit-exceeded" if not.
- The contract will update lastAmount to currentRateLimit minus amountToDecrease and set lastUpdated to the current block timestamp.
- The contract will emit a RateLimitDecreaseTriggered event with the key, amountToDecrease, currentRateLimit, and newLimit.
- The contract will return the newLimit.

The function call is as follows:

`function triggerRateLimitDecrease(bytes32 key, uint256 amountToDecrease) external override onlyRole(CONTROLLER) returns (uint256 newLimit)`
