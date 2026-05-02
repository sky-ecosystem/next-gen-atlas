---
id: 493bc01d-1c2e-4ef1-8605-1183c77a8cf2
docNo: A.6.1.1.2.2.6.1.2.2.1.6.6
name: Tokenized Treasury Redeemer Contract Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.6.6 - Tokenized Treasury Redeemer Contract Role [Core]

The `REDEEMER_CONTRACT_ROLE` on a Tokenized Treasury Instance is granted to authorized redeemer contracts that execute the two-step redemption of credit tokens on behalf of holders of the `REDEEMER_ROLE`. `REDEEMER_CONTRACT_ROLE` holders are added and removed via the `addTokenRedeemer` and `removeTokenRedeemer` functions, which are authorized for the `MANAGER_ADMIN_ROLE`.
