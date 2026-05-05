---
id: 0338eae8-0c00-4eb4-858f-50d66f2c65d7
docNo: A.6.1.1.2.2.6.1.3.1.4.1.3.2.2
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.3.1.4.1.3.2.2 - Encode Function [Core]

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `setDelegatedSigner` function to set the address that will be authorized as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.setDelegatedSigner, (address(delegatedSigner)))
    );
}`
