---
id: 09de757a-e742-4061-a1d4-7e5d70e9c0df
docNo: A.6.1.1.1.2.6.1.2.2.3.4.3
name: Aave AToken Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.4.3 - Aave AToken Withdrawal Action [Core]

In order to withdraw all Aave AToken balances, the operator must execute the following action:

`mainnetController.withdrawAave(aToken, aToken.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).
