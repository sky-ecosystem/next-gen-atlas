---
id: 8838da61-5edf-4ad5-b910-d4536aecd822
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.3.1
name: Set The Maximum Slippage Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.3.1 - Set The Maximum Slippage Function [Core]

Only an operator with the admin role is able to set the maximum slippage for a pool. To do so, they must call the `setMaxSlippage` function on the Controller contract on mainnet, providing the pool address and the maximum slippage value. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the maximum slippage for the specified pool.
- The contract will emit a `MaxSlippageSet` event to the blockchain logs.

The function call is as follows:

`function setMaxSlippage(address pool, uint256 maxSlippage) external`
