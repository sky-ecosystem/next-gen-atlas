---
id: 533d7220-75e3-43aa-8f1b-5512fdb9b828
docNo: A.6.1.1.2.2.6.1.2.2.1.3.3
name: Set Unlimited RateLimit
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.3.3 - Set Unlimited RateLimit [Core]

The following code sets out instructions for the operator to set an unlimited `RateLimit` for a specific key:

`function setUnlimitedRateLimitData(bytes32 key) external override {
        setRateLimitData(key, type(uint256).max, 0, type(uint256).max, block.timestamp);`
