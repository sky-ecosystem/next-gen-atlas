---
id: 85d7a1f5-3361-49cf-b087-b027183cb640
docNo: A.6.1.1.6.2.6.1.3.1.1.1.3.1.2
name: Call CancelMapleRedemption Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.3.1.1.1.3.1.2 - Call CancelMapleRedemption Function [Core]

Only an operator with the relayer role can cancel a previously requested redemption of shares from Maple. To do so, they must call the `cancelMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to cancel. All Maple cancellations of redemption operations are performed on behalf of the ALM Proxy. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will check that a rate limit exists for the asset. If no rate limit exists the transaction will revert.
- The contract will submit a cancellation request to the vault, removing the specified number of shares from the pending redemption.

The function call is as follows:

`function cancelMapleRedemption(address mapleToken, uint256 shares) external`
