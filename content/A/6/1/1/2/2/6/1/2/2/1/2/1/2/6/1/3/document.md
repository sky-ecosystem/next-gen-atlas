---
id: cedbc7ec-6356-4bf7-a5af-2c71353af7fd
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.3
name: Cancel Deposit Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.3 - Cancel Deposit Request [Core]

The operator must call the Centrifuge vault to `cancelDepositRequest` on behalf of the `proxy`. These cancelation methods are compatible with ERC-7887, and while the cancelation is pending no new deposit request can be submitted.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).cancelDepositRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy))
            )
        );
    }`
