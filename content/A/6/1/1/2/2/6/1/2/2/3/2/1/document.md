---
id: 8991b422-bd6b-4ea1-b0b9-b787ee4b1000
docNo: A.6.1.1.2.2.6.1.2.2.3.2.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`mainnetController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure](7b560160-e427-45a2-a3ac-3c23cf6fe943) and [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](7e90e505-42b9-474d-9cc5-9b4da6af7375).
