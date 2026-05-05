---
id: da2e149b-e70c-4373-94da-6da6c4c26048
docNo: A.6.1.1.1.2.6.1.2.2.1.1.1
name: Default Admin Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.1.1 - Default Admin Role [Core]

The admin role (`DEFAULT_ADMIN_ROLE`) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Spark Proxy.

`constructor(address admin) {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);`
