---
id: 6078cd75-f853-49ca-b7c1-eaab4ef85c72
docNo: A.6.1.1.5.2.6.1.2.2.3.2.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.5.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions](08d30ec2-c343-4176-aded-dce33e76d69c).
