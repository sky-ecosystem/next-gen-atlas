---
id: 872a4857-504e-4795-9cbd-2a6f159c1ea0
docNo: A.6.1.1.6.2.6.1.2.2.3.2.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions](c6dcf1ab-9861-4a41-9edc-ea79b705db2d).
