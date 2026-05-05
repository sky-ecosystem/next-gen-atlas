---
id: 41d9ae0a-c3a6-4a24-ae6a-b2ee841fb03d
docNo: A.3.3.2.7.1.1.1.6.0.3.1
name: BuyGem - Element Annotation
type: Annotation
depth: 12
childType: annotations
---

###### A.3.3.2.7.1.1.1.6.0.3.1 - BuyGem - Element Annotation [Annotation]

`buyGem` is a function that can be called on the LitePSM smart contract to buy a collateral asset in exchange for Dai. "Gem" here is Daiwanese for the collateral token.

The Lite Peg Stability Module maintains a pool of pre-minted Dai and Stablecoins to minimize transaction costs in swapping. The `buf` parameter is the amount of pre-minted Dai the LitePSM is designed to maintain in most instances. However, when a user calls `buyGem` and buys the collateral asset in exchange for Dai, the amount of Dai can temporarily exceed the `buf` parameter.
