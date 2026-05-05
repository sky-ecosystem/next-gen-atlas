---
id: 2a0d2948-5e23-4fc4-bad5-c692644f58c7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.1
name: Encode Transfer Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.1 - Encode Transfer Function [Core]

The operator must encode the `transfer` function call, using `abi.encodeCall` with the `buffer` address USDS will be transferred from, the `proxy` address that will receive USDS (i.e. ALM Proxy), and the `amount` of USDS to `transfer`.
