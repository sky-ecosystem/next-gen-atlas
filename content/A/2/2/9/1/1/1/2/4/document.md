---
id: e50fd86a-ffa4-4387-b212-420730a8d171
docNo: A.2.2.9.1.1.1.2.4
name: Outflow Rate Limits
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.1.2.4 - Outflow Rate Limits [Core]

Outflow Rate Limits constrain the rate at which allocated liquidity can be withdrawn or exposure reduced from a scope. "Outflow" means movements that lower exposure or capital allocated to an Instance or market, such as withdrawals, redemptions, or unwind operations.

Outflow limits are often configured more permissively to prioritize safety and fast exits. When outflow limits are "unlimited," the rate limits contract simply does not apply a cap in that direction.
