---
id: 79ba7e11-2adf-45fa-a73f-4c20ba1efc27
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.6.2
name: Send Encoded Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.6.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` specifying the `address` of the `asset` contract they want to deposit into.

       `// Approve underlying to Aave pool from the proxy (assumes the proxy has enough underlying).
proxy.doCall(
address(underlying),
abi.encodeCall(underlying.approve, (address(pool), amount))
);`
