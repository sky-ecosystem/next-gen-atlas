---
id: 1cb17b82-a294-4942-8183-4d90b224a79d
docNo: A.2.2.10.1.1.1.5.3.1
name: RateLimits Query
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.3.1 - RateLimits Query [Core]

The following code implements the public view functions that query the current `RateLimits` for a specific key:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory) {
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
