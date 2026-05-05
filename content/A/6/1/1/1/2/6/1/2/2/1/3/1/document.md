---
id: 89577062-a38b-4cf7-a1ae-33c0bcff1cca
docNo: A.6.1.1.1.2.6.1.2.2.1.3.1
name: RateLimits Query
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.3.1 - RateLimits Query [Core]

The following code sets out instructions for the operator to query the current `RateLimits` for a specific key:

`Function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory) {
        return _data[key];
    }

    function getCurrentRateLimit(bytes32 key) public override view returns (uint256) {
        RateLimitData memory d = _data[key];

        // Unlimited rate limit case
        if (d.maxAmount == type(uint256).max) {
            return type(uint256).max;
        }

        return _min(
            d.slope * (block.timestamp - d.lastUpdated) + d.lastAmount,
            d.maxAmount
        );
    }`
