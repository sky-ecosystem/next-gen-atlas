---
id: 742945a7-1031-483f-873c-6bd229b58b4c
docNo: A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.2
name: Withdraw From PSM
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.2 - Withdraw From PSM [Core]

The operator, acting as a Relayer, calls `withdrawPSM` to withdraw up to `maxAmount` of `asset` from the PSM to the ALM Proxy, returning the amount actually withdrawn as `assetsWithdrawn`. The withdrawn amount is then applied against the `LIMIT_PSM_WITHDRAW` rate limit for the asset. Only an address holding the `RELAYER` role may call this function.

`function withdrawPSM(address asset, uint256 maxAmount)
        external
        onlyRole(RELAYER)
        returns (uint256 assetsWithdrawn)`
