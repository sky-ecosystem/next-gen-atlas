---
id: ed445f2b-9211-46fe-b79a-6e70cac7fec7
docNo: A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.1.1
name: Call swapUSDSToDAI Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.1.1 - Call swapUSDSToDAI Function [Core]

Only an operator with the relayer role can swap USDS to Dai. To do so, they must call the `swapUSDSToDAI` function on the Controller contract on mainnet, providing the usdsAmount. The operation will only succeed if the Proxy holds enough USDS for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified USDS amount from the Proxy.
- The contract will swap USDS to Dai at a 1:1 ratio by calling the `usdsToDai` function on the migrator, sending the resulting DAI to the proxy.

The function call is as follows:

`function swapUSDSToDAI(uint256 usdsAmount) external`
