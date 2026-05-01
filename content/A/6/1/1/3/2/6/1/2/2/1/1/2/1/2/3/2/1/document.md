---
id: 37c09b7c-6aa0-4c3c-861e-984de4e3ba4d
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.2.1
name: Call withdrawERC4626 Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.2.1 - Call withdrawERC4626 Function [Core]

Only an operator with the relayer role can withdraw assets from an ERC-4626 vault. To do so, call the `withdrawERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to withdraw. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for withdrawal; otherwise, the transaction will revert. When this function is called:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the withdrawal amount is within the allowed rate limit for the specified vault.
- The contract will withdraw the specified amount from the vault, burning the necessary number of vault shares held by the ALM Proxy as part of the withdrawal process.
- The withdrawn assets will be sent to the ALM Proxy.

The function call is as follows:

`function withdrawERC4626(address token, uint256 amount) external returns (uint256 shares)`
