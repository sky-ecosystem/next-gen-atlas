---
id: 5592661d-78e9-4185-9c6e-15ffa47e0aef
docNo: A.2.2.10.1.1.1.5.2.3
name: Deposit To Aave Market
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.3 - Deposit To Aave Market [Core]

The documents herein define the steps to deposit an asset held by the ALM Proxy into an Aave v3 market, minting aTokens to the ALM Proxy. The deposit is performed by calling the Diamond PAU Controller, specifying the market and the amount to deposit; the Controller dispatches the call to the Aave Facet.
