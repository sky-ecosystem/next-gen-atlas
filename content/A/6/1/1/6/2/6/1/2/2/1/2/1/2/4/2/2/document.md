---
id: 0c3a819b-f93f-4565-948f-7d9147cfe9d8
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.2.2
name: Call claimRedeemERC7540 Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.2.2 - Call claimRedeemERC7540 Function [Core]

Only an operator with the relayer role can claim assets from an ERC-7540 vault after a redemption request. To do so, they must call the `claimRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum amount of assets that can be claimed by the ALM Proxy.
- The contract will claim the assets from the vault, and the ALM Proxy will receive the corresponding amount of underlying assets.

The function call is as follows:

`function claimRedeemERC7540(address token) external`
