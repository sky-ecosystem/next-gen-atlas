---
id: 530a40e2-8322-44ff-b2ce-4ea0821a8b80
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.2.1.1
name: Call transferAsset Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.2.1.1 - Call transferAsset Function [Core]

Only an operator with the relayer role is able to transfer ERC-20 assets. To do so, they must call the `transferAsset` function on the Controller contract on mainnet, providing the ERC20 asset address, the destination address, and the amount to transfer. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `Rate Limits` allow for transferring the specified amount of the asset to the destination. If the transfer amount does not fall within the available Rate Limit, the transaction will revert.
- The contract will execute the ERC-20 `transfer` function, sending the specified amount of the asset to the destination address.

The function call is as follows:

`function transferAsset(address asset, address destination, uint256 amount) external`
