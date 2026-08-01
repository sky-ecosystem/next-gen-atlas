---
id: 82e54145-e633-4c73-bf11-948df17267be
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.2 - Check RateLimits [Core]

The operator must ensure that `RateLimits` allows for redeeming the requested `shares` from the ERC-7540 vault. The rate limit is keyed to the specific `token` and is decreased by the asset-equivalent value of the `shares`, obtained by calling `convertToAssets` on the vault.

`        _rateLimitedAsset(
            LIMIT_7540_REDEEM,
            token,
            IERC7540(token).convertToAssets(shares)
        );`
