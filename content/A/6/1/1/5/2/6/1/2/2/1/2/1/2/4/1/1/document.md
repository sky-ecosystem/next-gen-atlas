---
id: 134e3124-3ba1-43dc-a3e6-9347416f006b
docNo: A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.1.1
name: Call requestDepositERC7540 Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.1.1 - Call requestDepositERC7540 Function [Core]

Only an operator with the relayer role can request a deposit into an ERC-7540 vault. To do so, they must call the `requestDepositERC7540` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The Rate Limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will submit a deposit request to the vault. Shares will not be received immediately; they must be claimed in a separate step after the vault processes the deposit.

The function call is as follows:

`function requestDepositERC7540(address token, uint256 amount) external`
