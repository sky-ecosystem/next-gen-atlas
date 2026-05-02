---
id: b46d9837-cca9-4d36-8363-a32379d28f93
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.4.1
name: Encode Transfer Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.4.1 - Encode Transfer Function [Core]

The operator must encode the `transfer` function call, using `abi.encodeCall` with the `buffer` address USDS will be transferred from, the `proxy` address that will receive USDS (i.e. ALM Proxy), and the `amount` of USDS to `transfer`.
