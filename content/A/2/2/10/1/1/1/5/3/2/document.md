---
id: f671061e-11a0-4d3b-bb6e-9f4ee9a012a9
docNo: A.2.2.10.1.1.1.5.3.2
name: Set RateLimit
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.3.2 - Set RateLimit [Core]

The following code sets the `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy):

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
