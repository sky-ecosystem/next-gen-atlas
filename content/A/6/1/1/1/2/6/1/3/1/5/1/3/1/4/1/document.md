---
id: a2430308-7a82-457e-b505-ea9889bf90d5
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.1 - Encode Function Call [Core]

The operator must encode the function call to the ERC-4626 `approve` method, using `abi.encodeCall` to allow the `token` address (`[Instance_Fluid_USDS_Vault_Address_Placeholder`]) spend up to `amount` of a token from ALM Proxy’s balance.
