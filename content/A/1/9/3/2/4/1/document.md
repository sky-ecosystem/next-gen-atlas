---
id: a228410a-353b-45dc-8f26-aae54ad8bf44
docNo: A.1.9.3.2.4.1
name: Liquidations Circuit Breaker Exception Price Tolerance
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.9.3.2.4.1 - Liquidations Circuit Breaker Exception Price Tolerance [Core]

Breaker Price Tolerance is a parameter which determines the condition for the permissionless activation of circuit breaker. Adjusting the Breaker Price Tolerance requires an Executive Vote, which is subject to GSM Pause Delay.

The Breaker Price Tolerance is expressed as a number between zero and one, and works with the following equation: `next_oracle_price < current_oracle_price * breaker_price_tolerance`.

In instances where the price oracle model does not support the price delay function, the permissionless activation of the liquidation circuit breaker ceases to function, since there is no next oracle price.
