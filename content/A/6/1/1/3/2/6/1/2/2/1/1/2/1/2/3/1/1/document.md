---
id: 4e2c13af-7f66-4b87-9662-693e94212c28
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.1.1
name: Call depositERC4626 Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.1.1 - Call depositERC4626 Function [Core]

Only an operator with the relayer role can deposit assets into an ERC-4626 vault. To do so, they must call the `depositERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will deposit the specified amount into the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function depositERC4626(address token, uint256 amount) external returns (uint256 shares)`
