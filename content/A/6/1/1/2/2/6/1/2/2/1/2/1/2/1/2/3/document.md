---
id: 2e633940-12fd-4a3b-9b02-6fae976fd7e5
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3
name: Transfer USDS To Buffer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3 - Transfer USDS To Buffer [Core]

The operator returns `usdsAmount` of USDS from the `proxy` to the buffer via `ERC20Lib.transfer`, which has the `proxy` call `transfer` on the USDS contract and requires the transfer to succeed.

`// Transfer USDS from the proxy to the buffer
        ERC20Lib.transfer(proxy, address(usds), buffer, usdsAmount);`
