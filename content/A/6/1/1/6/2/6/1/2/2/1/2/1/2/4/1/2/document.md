---
id: fccd0af9-6156-400e-bb4b-27a9d4fca711
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.1.2
name: Call claimDepositERC7540 Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.1.2 - Call claimDepositERC7540 Function [Core]

Only an operator with the relayer role can claim shares from an ERC-7540 vault after a deposit request. To do so, they must call the `claimDepositERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum number of shares that can be claimed by the ALM Proxy.
- The contract will claim the shares from the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function claimDepositERC7540(address token) external`
