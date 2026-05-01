---
id: eea8794f-8067-4f97-b03a-ae654d0793a8
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.1.3
name: Check RateLimits
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.3 - Check RateLimits [Core]

The operator must ensure the `deposit` amount is allowed within the `RateLimits` for this instance (e.g., using `[Instance_RateLimitID_Deposit_Placeholder]` for `token [Instance_Fluid_USDS_Vault_Address_Placeholder]`).

`        rateLimited(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Deposit_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),,
            amount
        )
        returns (uint256 shares)
    {
        // Note that whitelist is done by rate limits
        IERC20 asset = IERC20(IERC4626([Instance_Fluid_USDS_Vault_Address_Placeholder]).asset());`
