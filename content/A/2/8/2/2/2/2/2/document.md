---
id: f97cc4c7-d0d5-47fc-9f86-c00824ae6d7f
docNo: A.2.8.2.2.2.2.2
name: Borrow Rate Mechanism
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.2.8.2.2.2.2.2 - Borrow Rate Mechanism [Core]

The borrow rate subsidy for Spark and Grove will be calculated according to the formula: `SOFR + ((Base_Rate - SOFR) * T/24)`, where SOFR is specified in [A.3.3.2.2.4.1.3 - Secured Overnight Financing Rate](2edd1333-6ca6-4c10-9d71-80b85d4a4265), T represents elapsed months and is a counter that increases monthly over the 2-year period.
