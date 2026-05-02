---
id: 2bcdc1c9-6e43-4059-8a46-0a68c17f487d
docNo: A.3.7.1.1.2.5.2
name: Auction Price Multiplier (buf)
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.7.1.1.2.5.2 - Auction Price Multiplier (buf) [Core]

The `buf` parameter is a multiplier that is applied to the starting price of a collateral auction. Each vault type has its own Auction Price Multiplier that can be adjusted by Sky Governance separately. This multiplier is intended to be greater than 1.0x because Liquidations 2.0 uses falling price auctions. This means that it is generally preferable for the auction price to begin above the market price and then fall to the correct value over some amount of time. The `buf` parameter is defined as a multiplicative factor.
