---
id: 41cdf6f8-78c7-4aa0-8675-060fecf24d42
docNo: A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.1
name: Deposit To PSM
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.1 - Deposit To PSM [Core]

The operator, acting as a Relayer, calls `depositPSM` to deposit `amount` of `asset` from the ALM Proxy into the PSM, receiving the corresponding PSM `shares` in return. The function approves the PSM to spend the `asset` from the ALM Proxy and then deposits it, crediting the shares to the ALM Proxy. Only an address holding the `RELAYER` role may call this function, and the deposit is rate limited per asset by `LIMIT_PSM_DEPOSIT`.

`function depositPSM(address asset, uint256 amount)
        external
        onlyRole(RELAYER)
        rateLimitedAsset(LIMIT_PSM_DEPOSIT, asset, amount)
        returns (uint256 shares)`
