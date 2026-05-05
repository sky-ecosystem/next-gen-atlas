---
id: 569e1c2b-0e69-43e7-8491-06cc5f7d2988
docNo: A.2.2.6.2
name: Upkeep Rebate Primitive
type: Core
depth: 5
childType: sections_and_primary_docs
---

###### A.2.2.6.2 - Upkeep Rebate Primitive [Core]

The Upkeep Rebate Primitive allows a Prime Agent ("Holding Agent") to claim a rebate on its Ecosystem Upkeep Fees when it holds any portion of the token supply of another Prime Agent ("Issuing Agent").

Ecosystem Upkeep Fees are accounted on a monthly basis. The Upkeep Rebate is calculated on the same cadence per Holding Agent as follows:

1. The Holding Agent’s share of the Issuing Agent’s token supply at the time the Issuing Agent pays its Ecosystem Upkeep Fees, multiplied by
2. The total monthly Ecosystem Upkeep Fees paid by the Issuing Agent, calculated as specified in [A.2.2.6.1.2 - Valuation](4b856873-8c6a-449a-8ca6-487d8fed9029).

This resulting rebate amount is applied against the Holding Agent’s Ecosystem Upkeep Fees due in the calendar month immediately following the Issuing Agent’s payment.
