---
id: 98208afa-5810-4591-b261-efe0c1b882e5
docNo: A.6.1.1.3.2.6.1.2.2.1.3.2.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.3.2.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3 - ERC-4626 Functions](3de32801-e895-4a21-84da-aa5818d16349).
