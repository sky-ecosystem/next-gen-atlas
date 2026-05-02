---
id: a6f085f5-4670-443e-ad83-b538527b8c24
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMintRecipient`.

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
