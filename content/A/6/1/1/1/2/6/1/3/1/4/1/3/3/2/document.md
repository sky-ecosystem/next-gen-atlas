---
id: 71d2f286-960f-4264-86db-b48154f38366
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.3.2
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.3.2 - Encode Function [Core]

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `removeDelegatedSigner` function to remove the authorization for the `address` to act as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.removeDelegatedSigner, (address(delegatedSigner)))
    );
}`
