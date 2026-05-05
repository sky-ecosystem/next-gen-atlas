---
id: aec1d10f-a5df-48d4-bbea-1b02c279c919
docNo: A.6.1.1.2.2.6.1.2.2.1.3.2
name: Set RateLimit
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.3.2 - Set RateLimit [Core]

The following code sets out instructions for the operator to set the `RateLimit` for a specific key:

`function setRateLimitData(
        bytes32 key,
        uint256 maxAmount,
        uint256 slope,
        uint256 lastAmount,
        uint256 lastUpdated
    )
        public override onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(lastAmount  <= maxAmount,       "RateLimits/invalid-lastAmount");
        require(lastUpdated <= block.timestamp, "RateLimits/invalid-lastUpdated");

        _data[key] = RateLimitData({
            maxAmount:   maxAmount,
            slope:       slope,
            lastAmount:  lastAmount,
            lastUpdated: lastUpdated
        });

        emit RateLimitDataSet(key, maxAmount, slope, lastAmount, lastUpdated);
    }

    function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override {
        setRateLimitData(key, maxAmount, slope, maxAmount, block.timestamp);
    }`
