---
id: f92ddc3f-672a-4f52-931f-5263a9f709b9
docNo: A.6.1.1.1.2.6.1.2.2.3.4.1
name: ERC-4626 Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action [Core]

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`mainnetController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure](e797d1cc-9161-4b7a-8c16-db20a026d001) and [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](ed774ab7-c761-444b-963d-7407bf91e243).
