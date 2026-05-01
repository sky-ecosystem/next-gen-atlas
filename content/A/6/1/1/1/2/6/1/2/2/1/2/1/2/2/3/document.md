---
id: ed774ab7-c761-444b-963d-7407bf91e243
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3
name: General Redeem from ERC-4626 Tokens Procedure
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure [Core]

This document defines the steps for an operator to redeem yield-bearing shares from the ERC-4626 vault, receiving the corresponding amount of underlying assets into the ALM Proxy.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a redemption of shares.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient shares of the ERC4626 vault token.
- The Spark Liquidity Layer Operator calls the `redeem(uint256 shares, address receiver, address owner)` function on the target ERC4626 vault, specifying the number of `shares` to redeem, with the ALM `proxy` as both `receiver` (of assets) and `owner` (of shares being redeemed).
- The amount of underlying assets received is recorded, and relevant `RateLimits` (for withdrawal) are updated.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific ERC4626 Instance Configuration Document.
