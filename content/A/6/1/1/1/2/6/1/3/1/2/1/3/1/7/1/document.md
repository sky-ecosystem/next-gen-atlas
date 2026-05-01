---
id: 7d5b7673-1d17-4d64-9777-9d584d99ada6
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.1
name: Encode Function Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.1 - Encode Function Call [Core]

The operator must encode the `deposit` function call, using `abi.encodeCall` with the address of the `underlying` token, the `amount` of the underlying asset to `deposit` and the `address(proxy)` that will receive the resulting `aTokens` (i.e. ALM Proxy).
