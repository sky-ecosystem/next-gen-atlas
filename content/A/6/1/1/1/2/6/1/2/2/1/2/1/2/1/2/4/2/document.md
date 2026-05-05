---
id: 5db8d9fd-015e-414e-a35e-450fea7f9e8b
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.4.2
name: Send Encoded Call
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.4.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `wipe` function of the vault contract.

`// Burn USDS from the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.wipe, (usdsAmount))
        );
    }`
