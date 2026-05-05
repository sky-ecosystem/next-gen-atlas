---
id: 0bc584c7-53da-47ee-9e7f-7514076e5fb0
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.1.2.1
name: Call setLayerZeroRecipient Function
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.2.1 - Call setLayerZeroRecipient Function [Core]

Only an operator with the admin role is able to set the LayerZero recipient for a destination endpoint. To do so, they must call the `setLayerZeroRecipient` function on the Controller contract on mainnet, providing the destination endpoint ID and the recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the selected LayerZero recipient for the specified destination endpoint.
- The contract will emit a `LayerZeroRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient) external`
