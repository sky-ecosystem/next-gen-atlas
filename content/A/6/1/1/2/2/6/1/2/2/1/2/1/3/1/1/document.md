---
id: 838e55d5-6673-42c0-a590-c0fb4501e078
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.1
name: Freezer Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.1 - Freezer Role [Core]

The operator must ensure they are working as a `FREEZER`. Only the `FREEZER` role is allowed to `removeRelayer`.

`function removeRelayer(address relayer)
        external
        onlyRole(FREEZER)`
