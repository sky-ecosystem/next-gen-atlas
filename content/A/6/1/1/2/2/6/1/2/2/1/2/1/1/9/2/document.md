---
id: 3129dc03-3fff-4f4d-86df-639689b2498e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.2
name: Validate Token Address
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.2 - Validate Token Address [Core]

The operator must ensure the `token` is not the zero address, reverting with `MainnetController/token-zero-address` otherwise.

`        require(token != address(0), "MainnetController/token-zero-address");`
