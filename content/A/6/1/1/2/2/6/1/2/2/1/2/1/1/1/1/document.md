---
id: 310f2d02-371c-4fa1-b0bf-1e07d80464ee
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMintRecipient`.

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
