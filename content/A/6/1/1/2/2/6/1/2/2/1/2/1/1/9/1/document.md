---
id: 4e999d40-1303-4e5a-98b4-45eb808c62e9
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMaxExchangeRate`.

`function setMaxExchangeRate(address token, uint256 shares, uint256 maxExpectedAssets) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`
