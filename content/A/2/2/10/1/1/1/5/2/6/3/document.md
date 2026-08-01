---
id: 25da7163-b052-459f-91b5-8da3aafa61c7
docNo: A.2.2.10.1.1.1.5.2.6.3
name: Withdraw Asset From Basin
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.5.2.6.3 - Withdraw Asset From Basin [Core]

The Basin Facet's `withdraw` function withdraws up to the specified maximum amount of the asset from the Basin to the ALM Proxy, burning the corresponding Basin shares. The withdrawal does not complete unless the assets received satisfy the specified minimum conversion rate (`minConversionRate`) relative to the shares burned.
