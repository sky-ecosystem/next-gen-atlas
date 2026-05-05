---
id: 9926982e-5571-4108-9caa-88b4d8708d45
docNo: A.6.1.1.5.2.6.1.2.2.1.2.1.1.3.1
name: Call setMaximumSlippage Function
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.3.1 - Call setMaximumSlippage Function [Core]

Only an operator with the admin role is able to set the maximum slippage for a pool. To do so, they must call the `setMaxSlippage` function on the Controller contract on mainnet, providing the pool address and the maximum slippage value. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the maximum slippage for the specified pool.
- The contract will emit a `MaxSlippageSet` event to the blockchain logs.

The function call is as follows:

`function setMaxSlippage(address pool, uint256 maxSlippage) external`
