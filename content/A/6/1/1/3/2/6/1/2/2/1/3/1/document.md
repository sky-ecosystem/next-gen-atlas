---
id: 00a56799-7803-460a-bda3-eab312fc296d
docNo: A.6.1.1.3.2.6.1.2.2.1.3.1
name: Remove Compromised Relayer As Freezer
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.3.1 - Remove Compromised Relayer As Freezer [Core]

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. Only an operator with the freezer role can remove a relayer. To do so, they must call the `removeRelayer` function on the Controller contract on mainnet, providing the compromised relayer’s address. Calling this function will carry out the following actions:

- The contract will confirm the caller holds the freezer role. If the caller does not have the freezer role, the transaction will revert.
- The contract will revoke the relayer role from the specified address.
- The contract will emit a `RelayerRemoved(relayer)` event.

The function call is as follows:

`function removeRelayer(address relayer) external`
