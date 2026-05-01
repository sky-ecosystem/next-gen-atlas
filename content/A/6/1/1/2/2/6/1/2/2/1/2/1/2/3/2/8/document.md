---
id: 20dba0ba-3dd2-47cb-8e7a-793de6a11c5d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.8
name: Split Into Multiple Swaps If Limit Exceeded
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.8 - Split Into Multiple Swaps If Limit Exceeded [Core]

If the `usdcAmount` exceeds the limit, the operator must split the swap into multiple smaller swaps as follows.

1. The operator must refill the PSM with DAI by calling `psm.fill()`.
2. The operator must recalculate the limit to see how much USDC can be swapped after the refill.
3. The operator must swap the maximum possible USDC amount that doesn't exceed the limit.
4. The operator must update `remainingUsdcToSwap` by subtracting the amount just swapped.
5. The operator must repeat the process until the full `usdcAmount` is swapped.
