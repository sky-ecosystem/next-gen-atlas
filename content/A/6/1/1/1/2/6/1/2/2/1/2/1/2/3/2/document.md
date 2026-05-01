---
id: 6e75a2bd-70b7-4081-bb9f-39cf6b321066
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2
name: General Withdraw from Aave ATokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure [Core]

This document defines the steps for an operator to withdraw from Aave lending pools.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a withdrawal from an Aave instance.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient `aTokens` for the instance, and the withdrawal amount is within instance-specific `RateLimits` (defined in the relevant Aave ICD).
- The Spark Liquidity Layer Operator identifies the `underlying` asset address and Aave `pool` address from the specific Aave ICD.
- The Spark Liquidity Layer Operator calls the `withdraw(address asset, uint256 amount, address to)` function on the Aave `pool`, providing the `underlying` asset address, `amount` to withdraw, and the ALM `proxy` address (as `to`).
- The amount of underlying assets withdrawn is recorded, and relevant `RateLimits` are updated.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific Aave ICD.
