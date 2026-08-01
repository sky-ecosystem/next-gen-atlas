---
id: b4560318-fad0-43cf-a218-7c777d3b924f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3AddLiquidityUpperTickBound`.

`function setUniswapV3AddLiquidityUpperTickBound(address pool, int24 upperTickBound)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
