---
id: 1bac7288-5cd8-4632-9ff1-ef98977f57d8
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.3
name: Transfer Asset To Destination
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.3 - Transfer Asset To Destination [Core]

The operator must call the `MainnetController` contract to `transfer` the `amount` of the `asset` from the Grove ALM Proxy to the `destination`. The transfer is executed through `proxy.doCall` and reverts unless the token's `transfer` returns empty or `true`.

`        ERC20Lib.transfer(proxy, asset, destination, amount);
    }`
