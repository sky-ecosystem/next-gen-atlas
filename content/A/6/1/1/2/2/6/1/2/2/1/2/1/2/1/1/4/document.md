---
id: b51fa176-1c34-4ad3-9154-46a6d1b6f60d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4
name: Transfer USDS To ALM Proxy
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4 - Transfer USDS To ALM Proxy [Core]

The operator moves the drawn USDS from the buffer to the `proxy` by having the `proxy` call `usds.transferFrom`, pulling `usdsAmount` from the buffer to the ALM Proxy.

`// Transfer USDS from the buffer to the proxy
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transferFrom, (buffer, address(proxy), usdsAmount))
        );`
