---
id: 9ef24c37-3164-437f-b0b6-2f19105022db
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `setDelegatedSigner`, which is enforced by the `_checkRole` check at the start of the function.

`function setDelegatedSigner(address delegatedSigner) external {
        _checkRole(RELAYER);`
