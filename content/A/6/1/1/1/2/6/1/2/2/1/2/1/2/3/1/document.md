---
id: 316008c1-0c1f-487a-a5bf-1966e86fb946
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.1
name: General Deposit to Aave ATokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.1 - General Deposit to Aave ATokens Procedure [Core]

This document defines the steps for an operator to deposit to Aave lending pools.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a deposit to an Aave instance.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient underlying asset, and the deposit amount is within instance-specific `RateLimits` (defined in the relevant Aave ICD).
- The Spark Liquidity Layer Operator identifies the `underlying` asset address and Aave `pool` address from the specific Aave ICD.
- The Spark Liquidity Layer Operator approves the Aave `pool` to spend the `underlying` asset from the ALM Proxy.
- The Spark Liquidity Layer Operator calls the `supply(address asset, uint256 amount, address onBehalfOf, uint16 referralCode)` function on the Aave `pool`, providing the `underlying` asset address, `amount`, ALM `proxy` address (as `onBehalfOf`), and referral code (typically 0).
- The ALM Proxy receives `aTokens` representing the deposited assets.
- For detailed call structures, instance-specific parameters (aToken address, underlying asset address, pool address, rate limits), and operational examples, refer to the specific Aave Instance Configuration Document (ICD) (e.g., [A.6.1.1.1.2.6.1.3.1.2.1.3 - Instance-specific Operational Processes](7895798c-50e2-4fa6-b4e9-5b9f259f822d) or other relevant Aave ICDs).
