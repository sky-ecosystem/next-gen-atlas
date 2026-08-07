---
id: 7ae5334c-61e6-41b9-b6a3-7ac3e61cc6a5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMaxSlippage`.

`function setMaxSlippage(address pool, uint256 maxSlippage)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
