---
id: 7b560160-e427-45a2-a3ac-3c23cf6fe943
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2
name: General Withdraw from ERC-4626 Tokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure [Core]

This document defines the steps for an operator to withdraw a yield-earning balance from the ERC-4626 vault to the ALM Proxy.

- The Grove Liquidity Layer Operator, acting as `RELAYER`, initiates a withdrawal.
- Pre-conditions are checked: Grove Liquidity Layer contract `isActive`, ALM Proxy has sufficient shares of the ERC4626 vault token, and the withdrawal amount is within instance-specific `RateLimits` (defined in the relevant ICD).
- Grove Liquidity Layer calls the `withdraw(uint256 assets, address receiver, address owner)` function on the target ERC4626 vault, specifying the `amount` of underlying assets to withdraw, with the ALM `proxy` as both `receiver` (of assets) and `owner` (of shares being burned).
- The number of shares burned is recorded.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific ERC4626 Instance Configuration Document.
