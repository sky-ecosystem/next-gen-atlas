---
id: 230f7b75-df50-417a-8d02-16089a5831c6
docNo: A.6.1.1.2.2.6.1.3.1.4.1.3.5.3
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.4.1.3.5.3 - Encode Function [Core]

The operator must use `proxy.doCall()` to send an approval call to the `usde` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(usde),
        abi.encodeCall(usde.approve, (address(ethenaMinter), usdeAmount))
    );
}`
