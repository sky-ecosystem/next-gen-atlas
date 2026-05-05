---
id: 516ca684-b183-4d57-9feb-97a7a9b58e42
docNo: A.6.1.1.2.2.6.1.3.1.4.2.3.3.2
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.4.2.3.3.2 - Encode Function [Core]

The operator must use `proxy.doCall()` to make a call to the `susde` contract to invoke the `unstake` function, which unstakes sUSDe and sends the resulting tokens back to the `proxy` address (i.e. ALM Proxy). They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.unstake, (address(proxy)))
    );
}`
