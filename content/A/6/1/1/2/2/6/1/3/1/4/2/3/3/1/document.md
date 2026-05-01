---
id: 1f19cb45-1934-4e2e-8d07-0d4b78e7188c
docNo: A.6.1.1.2.2.6.1.3.1.4.2.3.3.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.4.2.3.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function unstakeSUSDe()
        external
        onlyRole(RELAYER)
        isActive`
