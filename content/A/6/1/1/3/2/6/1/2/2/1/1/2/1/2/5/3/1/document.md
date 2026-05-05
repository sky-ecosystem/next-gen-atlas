---
id: f88e14a0-fa64-44cc-a52c-cb35b7704ee8
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.3.1
name: Call transferTokenLayerZero Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.3.1 - Call transferTokenLayerZero Function [Core]

Only an operator with the relayer role can transfer tokens via LayerZero. To do so, they must call the `transferTokenLayerZero` function on the Controller contract on mainnet, providing the oftAddress, amount, and destinationEndpointId (payable for native fees). The operation will only succeed if the ALM Proxy holds sufficient tokens and fees; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the transfer amount is within the allowed rate limit (built from LIMIT_LAYERZERO_TRANSFER, oftAddress, and destinationEndpointId).
- If approval is required, the contract will approve the token for the oftAddress.
- The contract will build LayerZero send options and a SendParam struct with destination details, amount, and recipient from layerZeroRecipients.
- The contract will quote the OFT receipt to set the minimum amount received.
- The contract will quote the messaging fee and execute the send via proxy.doCallWithValue, passing the fee value.

The function call is as follows:

`function transferTokenLayerZero(address oftAddress, uint256 amount, uint32  destinationEndpointId) external payable`
