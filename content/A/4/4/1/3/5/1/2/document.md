---
id: 05e97d4d-37e2-4ed8-acea-a8728fbe0402
docNo: A.4.4.1.3.5.1.2
name: Rate Setting Formula
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.4.4.1.3.5.1.2 - Rate Setting Formula [Core]

The Sky Borrow Rate is calculated according to the following formula when Utilization is less than or equal to Target Utilization:

`SKY Borrow Rate = SKY Borrow Minimum Rate + Utilization / Target Utilization * Slope 1`

The SKY Borrow Rate is calculated according to the following formula when Utilization is greater than Target Utilization:

`SKY Borrow Rate = SKY Borrow Minimum Rate + Slope 1 + (Utilization - Target Utilization) / (1 - Target Utilization) * Slope 2`
