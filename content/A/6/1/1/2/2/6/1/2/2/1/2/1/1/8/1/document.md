---
id: 60246e35-6a75-4640-8507-bae8aa5f813f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setCentrifugeRecipient`.

`function setCentrifugeRecipient(uint16 centrifugeId, bytes32 recipient) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`
