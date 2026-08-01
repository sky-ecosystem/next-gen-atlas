---
id: e2c8aec9-1ab9-4ac0-af1b-8e0dce1cef93
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeDelegatedSigner`, which is enforced by the `_checkRole` check at the start of the function.

`function removeDelegatedSigner(address delegatedSigner) external {
        _checkRole(RELAYER);`
