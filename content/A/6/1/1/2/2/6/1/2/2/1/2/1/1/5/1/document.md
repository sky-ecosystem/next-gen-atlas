---
id: 8dc5ac2f-1fda-476f-80bb-b6c05e924af3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3AddLiquidityLowerTickBound`.

`function setUniswapV3AddLiquidityLowerTickBound(address pool, int24 lowerTickBound)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
