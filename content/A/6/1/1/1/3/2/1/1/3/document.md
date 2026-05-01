---
id: 6ffdb8ee-b083-40f5-b51b-1c91e954b68b
docNo: A.6.1.1.1.3.2.1.1.3
name: SparkLend Risk Parameters Cap Automators
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.1.1.3 - SparkLend Risk Parameters Cap Automators [Core]

Cap Automators allow the Supply Cap defined in [A.6.1.1.1.3.2.1.1.1.9 - Supply Cap Definition](e222b8da-abda-42f5-8106-20c6f2881dc7) and the Borrow Cap defined in [A.6.1.1.1.3.2.1.1.1.10 - Borrow Cap Definition](a2d6a99e-c63a-4f30-87f3-a3d66b1eda92) to be dynamically adjusted.

The cap automator is defined in terms of three parameters:

1. `gap` - the target available exposure
2. `ttl` - the cooldown period for cap increases
3. `max` - the absolute maximum exposure

Authorized parties can update a covered Supply Cap or Borrow Cap so the available exposure is equal to the target, as long as the resulting exposure does not exceed the specified maximum limit and the cooldown period has elapsed in the case of increases to the Supply Cap or Borrow Cap.
