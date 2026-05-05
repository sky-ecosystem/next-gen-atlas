---
id: 862f4064-47e5-4f76-908d-64edfcfe0ddd
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.1
name: General Deposit to ERC-4626 Tokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.1 - General Deposit to ERC-4626 Tokens Procedure [Core]

This document defines the steps for an operator to deposit assets from the ALM Proxy to the ERC-4626 vault to receive yield-bearing shares.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a deposit.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient underlying asset, and the deposit amount is within instance-specific `RateLimits` (defined in the relevant Instance Configuration Document).
- The Spark Liquidity Layer Operator approves the target ERC4626 vault (identified by its `token` address in the Instance Configuration Document) to spend the underlying `asset` from the ALM Proxy.
- The Spark Liquidity Layer Operator calls the `deposit(uint256 amount, address receiver)` function on the target ERC4626 vault, specifying the `amount` of underlying asset and the ALM `proxy` as the receiver of vault shares.
- The number of shares received is recorded.
- For detailed call structures, instance-specific parameters (vault address, asset address, rate limits), and operational examples, refer to the specific ERC4626 Instance Configuration Document (ICD) (e.g., [A.6.1.1.1.2.6.1.3.1.5.1.3 - Instance-specific Operational Processes](3bc424bf-079e-4b6b-8749-58c942c7d57b) or other relevant ERC4626 ICDs).
