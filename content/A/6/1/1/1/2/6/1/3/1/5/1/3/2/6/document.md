---
id: 50c85778-c824-496b-ae01-7f8868ad341f
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.6
name: Decrease RateLimit
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.6 - Decrease RateLimit [Core]

The operator must decrease the `RateLimit` based on the assets redeemed.

`rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Withdraw_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),
            assets
        );
    }`
