---
id: 043d3c4c-7fa0-4bba-8393-ea762c109bce
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `transferFrom` function of the USDS contract.

`        // Transfer USDS from the buffer to the proxy
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transferFrom, (buffer, address(proxy), usdsAmount))
        );
    }`
