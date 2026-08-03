---
id: a85b7e8b-c4e9-44de-b717-efa4c8268d3b
docNo: A.2.2.10.1.1.1.5.3.3
name: Set Unlimited RateLimit
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.3.3 - Set Unlimited RateLimit [Core]

The following code sets an unlimited `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy):

`function setUnlimitedRateLimitData(bytes32 key) external override {
        setRateLimitData(key, type(uint256).max, 0, type(uint256).max, block.timestamp);
    }`
