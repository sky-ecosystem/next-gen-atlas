---
id: 078273b1-aac9-410d-849b-2e1898b1f784
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3PoolMaxTickDelta`.

`function setUniswapV3PoolMaxTickDelta(address pool, uint24 maxTickDelta) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`
