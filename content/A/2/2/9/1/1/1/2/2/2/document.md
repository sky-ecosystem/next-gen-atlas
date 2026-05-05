---
id: ae8674bc-44ac-4b95-b5df-c6322a1d6e9a
docNo: A.2.2.9.1.1.1.2.2.2
name: Slope
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.1.2.2.2 - Slope [Core]

`slope` is the linear refill rate of a rate limiter’s allowance over time. It defines how quickly the capacity to perform additional inflow or outflow accrues after prior consumption. For example, if the slope is set to 1,000,000 tokens per day (converted to per second for on-chain execution), the rate limit will recover at that rate until it reaches the maxAmount.
