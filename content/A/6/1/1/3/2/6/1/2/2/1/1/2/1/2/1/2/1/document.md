---
id: 59b093a0-9025-4c60-ba6f-7a2e78a35ed4
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2.1
name: Call burnUSDS Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2.1 - Call burnUSDS Function [Core]

Only an operator with the relayer role is able to repay vault debt and burn USDS. To do so, they must call the burnUSDS function of the Controller contract on mainnet with the amount of USDS that they wish to burn. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will increase the available Rate Limit for minting USDS by the amount of USDS being burned. This increase will be limited by the maxAmount parameter in the `Rate Limit` contract.
- The contract will transfer USDS from the proxy to the buffer.
- The contract will burn the USDS from the buffer and `wipe` an equivalent amount from the vault's debt.

The function call is as follows:

`function burnUSDS(uint256 usdsAmount) external`
