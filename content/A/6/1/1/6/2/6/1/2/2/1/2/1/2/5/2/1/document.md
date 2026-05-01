---
id: 06ba856a-91a7-43b5-b4d7-9f392df360d4
docNo: A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.2.1
name: Call swapDAIToUSDS Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.2.1 - Call swapDAIToUSDS Function [Core]

Only an operator with the relayer role can swap Dai to USDS. To do so, they must call the `swapDAIToUSDS` function on the Controller contract on mainnet, providing the daiAmount. The operation will only succeed if the Proxy holds enough Dai for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified Dai amount from the Proxy.
- The contract will swap Dai to USDS at a 1:1 ratio by calling the `daiToUsds` function on the migrator, sending the resulting USDS to the proxy.

The function call is as follows:

`function swapDAIToUSDS(uint256 daiAmount) external`
