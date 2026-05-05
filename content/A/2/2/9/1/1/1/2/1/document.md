---
id: a578830d-18f0-451c-8ff0-4a66094650ae
docNo: A.2.2.9.1.1.1.2.1
name: Rate Limiter
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.1.2.1 - Rate Limiter [Core]

Rate Limiter refers to the overall mechanism or system that limits the volume of token movements over time, implemented via the `RateLimits` contracts. The Rate Limiter manages multiple rate limits and enforces constraints on controller operations to prevent rapid asset drainage and mitigate risks from compromised relayers or other attacks. This ensures that the maximum amount of tokens processed within a specific time period stays within safe bounds. The `RateLimits` contracts and their addresses for each chain can be found in the Allocation System Primitive for a Prime, under ALM Contracts.
