---
id: 723f0161-d2aa-467c-9423-115afa55d14e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.3
name: Cancel Redeem Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.3 - Cancel Redeem Request [Core]

The operator must call the Centrifuge vault to `cancelRedeemRequest` on behalf of the `proxy`. These cancelation methods are compatible with ERC-7887, and while the cancelation is pending no new redeem request can be submitted.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).cancelRedeemRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy))
            )
        );
    }`
