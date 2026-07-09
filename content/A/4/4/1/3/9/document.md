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

1. The current price reported by [A.4.4.1.3.9.1 - SKY Price Oracle](7e9cf614-291d-43a5-984e-4f3366f42052).
2. The `cap` parameter as specified in [A.4.4.1.3.9.2 - Cap Parameter](532ed9cb-51de-4ac2-ade9-58c07b3ea3d5).
