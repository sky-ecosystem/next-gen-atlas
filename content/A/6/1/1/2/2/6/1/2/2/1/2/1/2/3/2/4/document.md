---
id: 2c2b3e9a-5135-4379-bd4f-9f52884bd8da
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4
name: Swap USDC To DAI
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4 - Swap USDC To DAI [Core]

The operator must swap USDC to DAI through the PSM using `sellGemNoFee` (1:1, no fee), routed through the `_swapUSDCToDAI` helper. The PSM can only supply as much DAI as it currently holds, so the operation first computes the maximum USDC swappable in one call as the PSM's DAI balance divided by `psmTo18ConversionFactor`. If `usdcAmount` fits within that limit, a single swap is performed. Otherwise the operation repeatedly calls `psm.fill()` to top up the PSM's DAI, recomputes the limit, and swaps in chunks until the full `usdcAmount` is exchanged. If the PSM cannot be filled enough to cover the full amount, `psm.fill()` reverts with `DssLitePsm/nothing-to-fill`, so the operation only succeeds when the entire `usdcAmount` can be swapped.

`uint256 limit = params.dai.balanceOf(address(params.psm)) / params.psmTo18ConversionFactor;

        if (params.usdcAmount <= limit) {
            _swapUSDCToDAI(params.proxy, params.psm, params.usdcAmount);
        } else {
            uint256 remainingUsdcToSwap = params.usdcAmount;

            while (remainingUsdcToSwap > 0) {
                params.psm.fill();

                limit = params.dai.balanceOf(address(params.psm)) / params.psmTo18ConversionFactor;

                uint256 swapAmount = remainingUsdcToSwap < limit ? remainingUsdcToSwap : limit;

                _swapUSDCToDAI(params.proxy, params.psm, swapAmount);

                remainingUsdcToSwap -= swapAmount;
            }
        }`

Each chunk is swapped through the `_swapUSDCToDAI` helper.

`function _swapUSDCToDAI(IALMProxy proxy, IPSMLike psm, uint256 usdcAmount) internal {
        proxy.doCall(
            address(psm),
            abi.encodeCall(psm.sellGemNoFee, (address(proxy), usdcAmount))
        );
    }`
