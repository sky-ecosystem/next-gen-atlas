---
id: 0270b595-8957-4fb2-a9cd-2bc197dc3367
docNo: A.6.1.1.3.2.6.1.2.2.2.1.1.1
name: Default Admin Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role [Core]

The admin role is configured with the following permissions: `can_freeze_controller`, `can_unfreeze_controller`, `can_manage_permissions`, `can_suspend_permissions`, `can_manage_reserves_and_integrations`, `can_invoke_external_transfer`. This role can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Keel Proxy.

`constructor(address admin) {
_grantRole(DEFAULT_ADMIN_ROLE, admin);`
