---
id: b2ae94d5-bdca-4435-b8cd-8bdceac86823
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.3
name: Claim Canceled Redeem Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.3 - Claim Canceled Redeem Request [Core]

The operator must call the Centrifuge vault to `claimCancelRedeemRequest`, returning the canceled redeem shares to the `proxy`.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).claimCancelRedeemRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy), address(proxy))
            )
        );
    }`
