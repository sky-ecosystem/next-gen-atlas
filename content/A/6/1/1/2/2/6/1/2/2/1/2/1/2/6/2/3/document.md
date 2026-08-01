---
id: 09b2795e-e171-4756-9a41-db7f22ca9ae2
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.3
name: Claim Canceled Deposit Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.3 - Claim Canceled Deposit Request [Core]

The operator must call the Centrifuge vault to `claimCancelDepositRequest`, returning the canceled deposit assets to the `proxy`.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).claimCancelDepositRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy), address(proxy))
            )
        );
    }`
