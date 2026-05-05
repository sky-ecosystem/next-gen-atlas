---
id: 938f26c5-6028-420d-86bf-f41f5d7aeb7e
docNo: A.6.1.1.1.2.6.1.3.1.4.2.3.1.3
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1.3 - Encode Function [Core]

The operator must use `proxy.doCall()` to make a call to the `susde` contract, invoking the `cooldownAssets` function with the specified amount of sUSDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.cooldownAssets, (usdeAmount))
    );
}`
