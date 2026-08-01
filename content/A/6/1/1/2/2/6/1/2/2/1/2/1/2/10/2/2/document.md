---
id: c638b0e2-9986-48f8-9652-cda49296d85d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.2
name: Remove Delegated Signer On Ethena Minter
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.2 - Remove Delegated Signer On Ethena Minter [Core]

The operator must call the `MainnetController` contract to remove the `delegatedSigner` on the `ethenaMinter`. The call is executed against the Ethena minter through `proxy.doCall`, revoking the `delegatedSigner`'s authorization to sign mint and redeem orders on behalf of the Grove ALM Proxy.

`        proxy.doCall(
            address(ethenaMinter),
            abi.encodeCall(ethenaMinter.removeDelegatedSigner, (address(delegatedSigner)))
        );
    }`
