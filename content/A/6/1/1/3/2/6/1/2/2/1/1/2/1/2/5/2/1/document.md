---
id: 1b18072b-c409-4d2f-a333-1e5c3ae8ab90
docNo: A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2.1
name: Call swapUSDCToUSDS Function
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2.1 - Call swapUSDCToUSDS Function [Core]

Only an operator with the relayer role can swap USDC to USDS via the PSM. To do so, they must call the `swapUSDCToUSDS` function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the amount of USDC specified for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDC_TO_USDS) for the PSM.
- The contract will approve the PSM to spend the USDC from the ALM Proxy.
- The contract will calculate the swap limit per transaction based on the DAI balance held by the PSM, converting with psmTo18ConversionFactor.
- If the usdcAmount is less than or equal to the limit, the contract will perform a direct swap of USDC to DAI.
- If the usdcAmount exceeds the limit, the contract will split the swap into multiple smaller swaps: refill the PSM with DAI via psm.fill, recalculate the limit, swap the maximum allowed amount, update the remaining amount, and repeat until complete (reverting with "DssLitePsm/nothing-to-fill" if PSM cannot be filled).
- The contract will convert the USDC amount to a DAI amount, accounting for token decimal differences.
- The contract will approve the daiUsds contract to spend the DAI amount from the ALM Proxy.
- The contract will swap DAI to USDS at a 1:1 ratio via daiUsds, sending USDS to the proxy.

The function call is as follows:

`function swapUSDCToUSDS(uint256 usdcAmount) external`
