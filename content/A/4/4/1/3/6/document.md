---
id: fac38a01-4c67-4810-af22-3e7b2d855567
docNo: A.4.4.1.3.6
name: stUSDS Risk Parameters
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.4.4.1.3.6 - stUSDS Risk Parameters [Core]

The liquidation parameters for SKY-backed loans funded via stUSDS are:

- Liquidation Ratio: 120%
- `Calc`: StairstepExponentialDecrease
- `Tau`: 0 days
- `Tolerance`: 0.5
- `Cut`: 0.99
- `Step`: 60 seconds
- `Buf`: 120%
- `Cusp`: 40%
- `Tail`: 6,000 seconds
- `Chip`: 0.1%
- `Stopped`: 3
- `Tip`: 300 USDS
- `Chop`: 13%
- `Hole`: 250,000
- `Dust`: 30,000
