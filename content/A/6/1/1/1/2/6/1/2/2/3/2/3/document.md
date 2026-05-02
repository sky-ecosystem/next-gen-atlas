---
id: 2560adbb-4a5c-4c95-86cb-04647bb33836
docNo: A.6.1.1.1.2.6.1.2.2.3.2.3
name: Aave AToken Withdrawal Action
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.3.2.3 - Aave AToken Withdrawal Action [Core]

In order to withdraw all AToken balances, the operator must execute the following action:

`foreignController.withdrawAave(aToken, aToken.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.2.2.2.2 - Withdraw Aave ATokens](5b090e5a-a2e7-4548-a1b4-53be86db6516).
