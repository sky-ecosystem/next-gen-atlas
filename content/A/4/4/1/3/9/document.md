---
id: c0fbc4e6-754c-4838-aa27-4ef6226f2769
docNo: A.4.4.1.3.9
name: SKY-Backed Borrowing Capped OSM Wrapper
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.4.4.1.3.9 - SKY-Backed Borrowing Capped OSM Wrapper [Core]

In order to prevent excessive price spikes if there is high demand for leverage against SKY tokens, which could potentially lead to excessive USDS borrowing against SKY, a wrapper for the SKY OSM contract has been developed.

The wrapper enforces an upper limit on the price of SKY for the purposes of SKY-Backed Borrowing, which is set to be the minimum value of:

1. The current price reported by PIP_SKY.
2. The `cap` that has been set on the OSM wrapper contract.
