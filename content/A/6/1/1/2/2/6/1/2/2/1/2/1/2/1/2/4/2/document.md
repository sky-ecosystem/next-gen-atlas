---
id: d9ecb48d-6487-4c98-89c6-fabd4af60490
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `wipe` function of the vault contract.

`// Burn USDS from the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.wipe, (usdsAmount))
        );
    }`
