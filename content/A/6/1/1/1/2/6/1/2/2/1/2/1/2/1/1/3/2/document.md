---
id: a171748b-6070-4b76-bda0-2268e2e1938d
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.3.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.3.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `draw` function of the vault contract.

`    {
        // Mint USDS into the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.draw, (usdsAmount))
        );`
