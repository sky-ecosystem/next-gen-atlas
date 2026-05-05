---
id: 46a74cd0-5e4e-4ea6-8fe6-ab38a8930f32
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6.1.1
name: Call transferUSDCToCCTP Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6.1.1 - Call transferUSDCToCCTP Function [Core]

Only an operator with the relayer role can initiate a USDC transfer to a specified destination domain using CCTP, handling rate limits, approvals, and splitting large amounts if needed. It requires parameters like proxy, Rate Limits, cctp, usdc, rate limit IDs, mintRecipient, destinationDomain, and usdcAmount. To do so, they must call the `transferUSDCToCCTP` function on the Controller contract on mainnet. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will trigger a rate limit decrease for the CCTP limit ID and amount.
- The contract will trigger a rate limit decrease for a domain-specific key and amount.
- The contract will require that mintRecipient is not zero, reverting if it is.
- The contract will approve the CCTP contract to spend the USDC amount from the proxy, assuming that the proxy has enough USDC.
- The contract will retrieve the burn limit per message for the USDC address (if the amount is larger than the limit it must be split into multiple calls).
- If the usdcAmount exceeds the burn limit, the contract will initiate a CCTP transfer for the burn limit amount and subtract it from the remaining usdcAmount.
- If any usdcAmount remains after the loop, the contract will initiate a final CCTP transfer for that amount.

The function call is as follows:

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain) external`
