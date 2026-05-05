---
id: aad3683d-38d4-4e94-b2bf-88b408c2290e
docNo: A.6.1.1.1.2.6.1.2.2.3.2.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`foreignController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.2 - Withdraw ERC-4626 Tokens](c2bbf44a-496c-4cf6-b0f6-25f77e66465b) and [A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.3 - Redeem ERC-4626 Tokens](ab5eb90f-1007-4560-a0ea-1c25d433c602).
