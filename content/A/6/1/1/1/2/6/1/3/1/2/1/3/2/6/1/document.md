---
id: d0168bc6-231f-44b8-87f6-b1cad0d742cc
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.1 - Encode Function Call [Core]

The operator must encode the `withdraw` function using `abi.encodeCall` with the `underlying asset address` from the `aToken` contract, specifying which token is being withdrawn, the `amount` of the underlying asset to `withdraw`, and the `address(proxy)` of the recipient of the withdrawn assets (i.e. ALM Proxy).
