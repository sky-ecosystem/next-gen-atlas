---
id: 037d3def-39bc-4aaf-9c3d-69fb86245f35
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.3.1
name: Call redeemERC4626 Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.3.1 - Call redeemERC4626 Function [Core]

Only an operator with the relayer role can redeem vault shares for the underlying asset. To do so, they must call the `redeemERC4626` function on the Controller contract on mainnet, providing the number of shares to redeem. The address is the ALM Proxy acting as both the owner of the shares being redeemed and the receiver of the resulting assets. The operation will only succeed if the ALM Proxy holds at least the number of shares specified for redemption; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will redeem the specified number of shares from the vault, sending the resulting assets to the ALM Proxy.
- After redemption, the contract will update the withdrawal rate limit based on the amount of assets received.

The function call is as follows:

`function redeemERC4626(address token, uint256 shares) external returns (uint256 assets)`
