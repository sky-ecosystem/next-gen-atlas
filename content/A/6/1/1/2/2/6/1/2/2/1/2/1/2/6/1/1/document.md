---
id: 69881982-618e-46bc-9ffb-af5c673a06f9
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cancelCentrifugeDepositRequest`.

`function cancelCentrifugeDepositRequest(address token) external {
        _checkRole(RELAYER);`
