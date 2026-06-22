---
id: 5f3ad3bb-6708-4bb5-8f0a-100c9a404092
docNo: A.6.1.1.2.2.6.1.2.2.1.2.2.2
name: Withdraw From Basin
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.2.2 - Withdraw From Basin [Core]

The documents herein define the steps to withdraw up to a maximum amount of an asset from a Basin to the ALM Proxy, burning the corresponding Basin shares. The withdrawal is performed by calling the Diamond PAU Controller, specifying the Basin, the asset, the maximum amount to withdraw, and the minimum conversion rate (`minConversionRate`); the Controller dispatches the call to the Basin Facet.
