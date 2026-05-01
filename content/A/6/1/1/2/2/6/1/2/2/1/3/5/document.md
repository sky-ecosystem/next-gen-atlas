---
id: d1dbab82-8be1-41f4-a4a3-ddc3cd0a917c
docNo: A.6.1.1.2.2.6.1.2.2.1.3.5
name: Set Trigger For RateLimit Increase
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.3.5 - Set Trigger For RateLimit Increase [Core]

The following code sets out instructions for the operator to trigger an increase of a `RateLimit` for a specific key:

`function triggerRateLimitIncrease(bytes32 key, uint256 amountToIncrease)
        external override onlyRole(CONTROLLER) returns (uint256 newLimit)
    {
        RateLimitData storage d = _data[key];
        uint256 maxAmount = d.maxAmount;

        require(maxAmount > 0, "RateLimits/zero-maxAmount");
        if (maxAmount == type(uint256).max) return type(uint256).max;  // Special case unlimited

        uint256 currentRateLimit = getCurrentRateLimit(key);

        d.lastAmount = newLimit = _min(currentRateLimit + amountToIncrease, maxAmount);
        d.lastUpdated = block.timestamp;

        emit RateLimitIncreaseTriggered(key, amountToIncrease, currentRateLimit, newLimit);`
