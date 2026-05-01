---
id: 19e6bba4-8d6f-4d1c-95d5-000b2dbf948c
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.2.1
name: Call requestRedeemERC7540 Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.2.1 - Call requestRedeemERC7540 Function [Core]

Only an operator with the relayer role can request the redemption of shares from an ERC-7540 vault. To do so, they must call the `requestRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address and the number of shares to redeem. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestRedeemERC7540(address token, uint256 amount) external`
