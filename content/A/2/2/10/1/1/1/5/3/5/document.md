---
id: ee55aa72-1405-49cb-a7fe-3e8adc9ee64c
docNo: A.2.2.10.1.1.1.5.3.5
name: Set Trigger For RateLimit Increase
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.3.5 - Set Trigger For RateLimit Increase [Core]

The following code increases the `RateLimit` for a specific key, restricted to the `CONTROLLER` role (the Controller contract), called as allocations return the limit:

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

        emit RateLimitIncreaseTriggered(key, amountToIncrease, currentRateLimit, newLimit);
    }`
