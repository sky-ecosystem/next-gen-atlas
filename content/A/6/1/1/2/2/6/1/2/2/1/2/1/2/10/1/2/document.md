---
id: a542c364-ce22-44c3-816d-97742b2d6a8f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.2
name: Set Delegated Signer On Ethena Minter
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.2 - Set Delegated Signer On Ethena Minter [Core]

The operator must call the `MainnetController` contract to set the `delegatedSigner` on the `ethenaMinter`. The call is executed against the Ethena minter through `proxy.doCall`, authorizing the `delegatedSigner` to sign mint and redeem orders on behalf of the Grove ALM Proxy.

`        proxy.doCall(
            address(ethenaMinter),
            abi.encodeCall(ethenaMinter.setDelegatedSigner, (address(delegatedSigner)))
        );
    }`
