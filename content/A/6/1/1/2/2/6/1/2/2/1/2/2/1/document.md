---
id: 3578e6f3-7ae6-4b73-a1f9-eed628585ba3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.1
name: Deposit To Basin
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.1 - Deposit To Basin [Core]

The documents herein define the steps to deposit an amount of an asset held by the ALM Proxy into a Basin, minting Basin shares to the ALM Proxy. The deposit is performed by calling the Diamond PAU Controller, specifying the Basin, the asset, the amount to deposit, and the minimum number of shares to receive (`minSharesOut`); the Controller dispatches the call to the Basin Facet.
