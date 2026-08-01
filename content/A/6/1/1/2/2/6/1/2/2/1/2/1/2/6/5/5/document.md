---
id: 219de76c-8db5-457f-a6ad-297c04ef597f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.5
name: Get Spoke Address
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.5 - Get Spoke Address [Core]

The operator must resolve the `spoke` contract that initiates the cross-chain transfer, obtained from the vault's async redeem `manager`.

`address spoke = IAsyncRedeemManagerLike(
            ICentrifugeV3VaultLike(token).manager()
        ).spoke();`
