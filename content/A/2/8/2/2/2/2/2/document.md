---
id: f97cc4c7-d0d5-47fc-9f86-c00824ae6d7f
docNo: A.2.8.2.2.2.2.2
name: Borrow Rate Mechanism
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.2.8.2.2.2.2.2 - Borrow Rate Mechanism [Core]

The borrow rate subsidy for Spark and Grove will be calculated according to the formula: `t-bill_rate + ((base_rate - t-bill_rate) * T/24)`, where T represents elapsed months and is a counter that increases monthly over the 2-year period.
