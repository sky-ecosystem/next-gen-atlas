---
id: a0dff4ff-a21f-40a4-b774-c0483ac9c90d
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.3.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.3.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `transfer` function of the USDS contract.

`     {
        // Transfer USDS from the proxy to the buffer
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transfer, (buffer, usdsAmount))
        );`
