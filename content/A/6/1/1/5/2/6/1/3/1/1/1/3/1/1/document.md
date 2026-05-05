---
id: fd047e05-3239-434b-a5d8-81cd72ada783
docNo: A.6.1.1.5.2.6.1.3.1.1.1.3.1.1
name: Call RequestMapleRedemption Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.3.1.1.1.3.1.1 - Call RequestMapleRedemption Function [Core]

Only an operator with the relayer role can request the redemption of shares from Maple. To do so, they must call the `requestMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to request. All Maple redemption operations are performed on behalf of the ALM Proxy and the destination address is always set to the proxy by the contract. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault and decrease the rate limit for the redemption amount.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestMapleRedemption(address mapleToken, uint256 shares) external`
