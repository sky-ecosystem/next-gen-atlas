---
id: 5b77e7bb-5f31-48eb-9cdd-8fb799986788
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.3
name: Check RateLimits
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.3 - Check RateLimits [Core]

The operator must ensure the `withdraw` amount is allowed within the `RateLimits `for this instance (e.g. using `[Instance_RateLimitID_Withdraw_Placeholder]` for `token` `[Instance_Fluid_USDS_Vault_Address_Placeholder]`).

`// Check withdrawal limits.
        rateLimited(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Withdraw_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),
            amount
        )
        returns (uint256 shares)`
