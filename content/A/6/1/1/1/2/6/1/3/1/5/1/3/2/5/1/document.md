---
id: 13e8ea29-273a-45ce-9a61-10256fb7caf0
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.1 - Encode Function Call [Core]

The operator must encode the function call to the ERC-4626 `redeem` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault(`[Instance_Morpho_USDS_Vault_Address_Placeholder]`), the `shares` to `redeem` and the `address(proxy)` of the receiver of redeemed assets and the owner of shares being received (i.e. ALM Proxy).
