---
id: cdab9e7d-6a80-42a1-95fb-e4f72de7dbaf
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `transfer` function of the USDS contract.

`     {
        // Transfer USDS from the proxy to the buffer
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transfer, (buffer, usdsAmount))
        );`
