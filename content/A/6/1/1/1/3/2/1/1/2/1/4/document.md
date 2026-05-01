---
id: b1a1fb8a-29d7-4bbd-8204-25c74263c25d
docNo: A.6.1.1.1.3.2.1.1.2.1.4
name: WETH Risk Parameters
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.1.1.2.1.4 - WETH Risk Parameters [Core]

The current WETH risk parameters are:

- LTV: 85%
- Liquidation Threshold: 86%
- E-mode Category: ETH
- Liquidation Bonus: 5%
- Reserve Factor: 5%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 90%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: N/A
- Slope 1 Spread: -0.30%
- Slope 2: 120%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

The Slope 1 parameter for WETH is calculated based on the following formula:

slope 1 = stETH yield + slope 1 spread - base rate
