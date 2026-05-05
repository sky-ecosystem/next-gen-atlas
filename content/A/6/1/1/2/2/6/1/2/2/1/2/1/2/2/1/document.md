---
id: 4876005c-31a8-4be8-8133-e239bd0ac53b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1
name: General Deposit to ERC-4626 Tokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1 - General Deposit to ERC-4626 Tokens Procedure [Core]

This document defines the steps for an operator to deposit assets from the ALM Proxy to the ERC-4626 vault to receive yield-bearing shares.

- The Grove Liquidity Layer Operator, acting as `RELAYER`, initiates a deposit.
- Pre-conditions are checked: Grove Liquidity Layer contract `isActive`, ALM Proxy has sufficient underlying asset, and the deposit amount is within instance-specific `RateLimits` (defined in the relevant Instance Configuration Document).
- The Grove Liquidity Layer Operator approves the target ERC4626 vault (identified by its `token` address in the Instance Configuration Document) to spend the underlying `asset` from the ALM Proxy.
- The Grove Liquidity Layer Operator calls the `deposit(uint256 amount, address receiver)` function on the target ERC4626 vault, specifying the `amount` of underlying asset and the ALM `proxy` as the receiver of vault shares.
- The number of shares received is recorded.
- For detailed call structures, instance-specific parameters (vault address, asset address, rate limits), and operational examples, refer to the specific ERC4626 Instance Configuration Document (ICD).
