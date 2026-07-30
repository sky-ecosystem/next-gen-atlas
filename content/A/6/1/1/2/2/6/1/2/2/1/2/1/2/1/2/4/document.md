---
id: df488122-2d82-4a54-8285-b24b86eb2e49
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4
name: Burn USDS From Buffer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4 - Burn USDS From Buffer [Core]

The operator burns the returned USDS from the buffer by having the `proxy` call `vault.wipe` for `usdsAmount`, repaying Grove's USDS debt in the Sky Allocation Vault.

`// Burn USDS from the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.wipe, (usdsAmount))
        );`
