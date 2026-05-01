---
id: e8053d8a-c24c-4acc-a928-c57fdbe11810
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.1 - Encode Function Call [Core]

The operator must encode the function call to the ERC-4626 `withdraw` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault (`[Instance_Fluid_USDS_Vault_Address_Placeholder]`), the `amount` of the underlying asset to `withdraw` and the `address(proxy)` of the recipient of the withdrawn assets and the sender of the shares (i.e. ALM Proxy).
