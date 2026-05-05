---
id: 40875283-48ec-48f0-8b61-e45d33f976ab
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.2.1
name: Call withdrawERC4626 Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.2.1 - Call withdrawERC4626 Function [Core]

Only an operator with the relayer role can withdraw assets from an ERC-4626 vault. To do so, they must call the `withdrawERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to withdraw. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for withdrawal; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the withdrawal amount is within the allowed rate limit for the specified vault.
- The contract will withdraw the specified amount from the vault, burning the necessary number of vault shares held by the ALM Proxy as part of the withdrawal process.
- The withdrawn assets will be sent to the ALM Proxy.

The function call is as follows:

`function withdrawERC4626(address token, uint256 amount) external returns (uint256 shares)`
