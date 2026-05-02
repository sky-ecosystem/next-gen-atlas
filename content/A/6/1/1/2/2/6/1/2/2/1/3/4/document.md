---
id: bc991d91-b79f-488c-b5d7-d632898c676e
docNo: A.6.1.1.2.2.6.1.2.2.1.3.4
name: Set Trigger For RateLimit Decrease
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.3.4 - Set Trigger For RateLimit Decrease [Core]

The following code sets out instructions for the operator to trigger a decrease of a `RateLimit` for a specific key:

`function triggerRateLimitDecrease(bytes32 key, uint256 amountToDecrease)
        external override onlyRole(CONTROLLER) returns (uint256 newLimit)
    {
        RateLimitData storage d = _data[key];
        uint256 maxAmount = d.maxAmount;

        require(maxAmount > 0, "RateLimits/zero-maxAmount");
        if (maxAmount == type(uint256).max) return type(uint256).max;  // Special case unlimited

        uint256 currentRateLimit = getCurrentRateLimit(key);

        require(amountToDecrease <= currentRateLimit, "RateLimits/rate-limit-exceeded");

        d.lastAmount = newLimit = currentRateLimit - amountToDecrease;
        d.lastUpdated = block.timestamp;

        emit RateLimitDecreaseTriggered(key, amountToDecrease, currentRateLimit, newLimit);
    }`
