---
id: c1f708eb-7373-448d-a54c-b178d0fd909a
docNo: A.6.1.1.1.2.6.1.2.2.3.2.4
name: Aave AToken Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.2.4 - Aave AToken Withdrawal Action [Core]

In order to withdraw all AToken balances, the operator must execute the following action:

`foreignController.withdrawAave(aToken, aToken.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).
