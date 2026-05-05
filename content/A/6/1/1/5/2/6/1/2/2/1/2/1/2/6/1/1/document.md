---
id: 0ec7c5be-32a2-4d3b-b856-71face6612a9
docNo: A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.1.1
name: Call swapUSDSToUSDC Function
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.1.1 - Call swapUSDSToUSDC Function [Core]

Only an operator with the relayer role can swap USDS to USDC via the PSM. To do so, they must call the `swapUSDSToUSDC` function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the equivalent amount of USDS for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDS_TO_USDC) for the PSM.
- The contract will convert the USDC amount to an 18-decimal format using psmTo18ConversionFactor.
- The contract will approve the daiUsds contract to spend the converted amount from the ALM Proxy.
- The contract will swap USDS to Dai at a 1:1 ratio via daiUsds, sending Dai to the proxy.
- The contract will approve the PSM to spend the Dai.
- The contract will swap Dai to USDC at a 1:1 ratio with no fee via psm.buyGemNoFee, sending USDC to the proxy.

The function call is as follows:

`function swapUSDSToUSDC(uint256 usdcAmount) external`
