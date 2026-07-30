---
id: fae744c3-d737-44c3-bc85-3cb14b9dc031
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.2
name: Revoke Relayer Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.2 - Revoke Relayer Role [Core]

The operator must revoke the `RELAYER` role from the relayer address being removed so that it can no longer operate the contract.

`{
        _revokeRole(RELAYER, relayer);`
