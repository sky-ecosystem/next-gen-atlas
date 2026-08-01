---
id: 5e388832-64cb-424b-a36a-ef1dd3eeb22a
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3TwapSecondsAgo`.

`function setUniswapV3TwapSecondsAgo(address pool, uint32 twapSecondsAgo)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
