---
id: 4f454648-637e-442a-9f0f-314958d15915
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.5.3
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5.3 - Encode Function [Core]

The operator must use `proxy.doCall()` to send an approval call to the `usde` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(usde),
        abi.encodeCall(usde.approve, (address(ethenaMinter), usdeAmount))
    );
}`
