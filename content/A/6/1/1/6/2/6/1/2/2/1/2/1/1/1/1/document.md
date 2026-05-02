---
id: 929818fb-10b0-4520-ba00-5bc2f46815ed
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.1.1.1
name: Call setMintRecipient Function
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.1.1 - Call setMintRecipient Function [Core]

Only an operator with the admin role is able to set the mint recipient for a destination domain. To do so, they must call the `setMintRecipient` function on the Controller contract on mainnet providing the destination domain and the mint recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role the transaction will revert.
- The contract will set the selected mint recipient for the specified destination domain.
- The contract will emit a `MintRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient) external`
