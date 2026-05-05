---
id: 6eb71a3a-09b6-430d-9677-af0c3f9667f1
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.1 - Encode Function Call [Core]

The operator must encode the function call to ERC-4626 `deposit` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault (`[Instance_Fluid_USDS_Vault_Address_Placeholder]`), the `amount` of the underlying asset to `deposit` and the `address(proxy)` that will receive the resulting shares (i.e. ALM Proxy).
