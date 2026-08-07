---
id: 2674da52-7a73-447f-811e-7dd40d23559f
docNo: A.3.5.2.4.5
name: Operators
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.3.5.2.4.5 - Operators [Core]

The SBE-BEAM Operator is a Governance-whitelisted entity that can use the SBE-BEAM to alter the three Smart Burn Engine parameters within its control — the Kicker Lot Size (`kbump`), the SKY Accumulation Percentage (`burn`), and the Splitter Interval (`hop`). Changes to the `kbump` and `hop` parameters, and to their combined throughput, are limited by the `maxKbump`, `minHop`, and `maxRate` parameters, and every change is subject to the `tau` cadence. The `burn` parameter is not subject to the `maxKbump`, `minHop`, or `maxRate` bounds, which limit only the rate of accumulation, and is constrained only by the technical maximum specified in [A.3.5.2.4.4 - Technical Limitations](42ea8a7b-fb28-455e-8038-5fcf25250f17). The Operator can be changed by an Executive Vote.
