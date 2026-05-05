---
id: e6313c89-b401-468d-882b-bf5e57d0182c
docNo: A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.1.1
name: Call mintUSDS Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.1.1 - Call mintUSDS Function [Core]

Only an operator with the relayer role is able to mint USDS. To do so, they must call the `mintUSDS` function on the Controller contract on mainnet with the amount of USDS that is required for minting. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `Rate Limits` allow for minting the required amount. If the mint amount does not fall within the available Rate Limit the transaction will revert.
- The contract will reduce the Rate Limit by the amount of USDS minted in this transaction.
- The contract will mint the required USDS into the buffer contract.
- The contract will transfer the newly minted USDS from the buffer to the Proxy.

The function call is as follows:

`function mintUSDS(uint256 usdsAmount) external`
