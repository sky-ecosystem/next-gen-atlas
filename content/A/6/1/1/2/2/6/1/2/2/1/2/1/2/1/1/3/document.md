---
id: 8230c4c2-71d4-4d1b-800b-0684e2de136e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3
name: Draw USDS To Buffer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3 - Draw USDS To Buffer [Core]

The operator draws USDS from the Sky Allocation Vault into the buffer by having the `proxy` call `vault.draw` for `usdsAmount`.

`// Mint USDS into the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.draw, (usdsAmount))
        );`
