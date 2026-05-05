---
id: 5b50fe5d-22a9-4ea4-a9e1-de7feba453a3
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.9
name: Split Into Multiple Swaps If Limit Exceeded
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.9 - Split Into Multiple Swaps If Limit Exceeded [Core]

If the PSM can't be filled, the transaction reverts with `DssLitePsm/nothing-to-fill`.

`else {
    uint256 remainingUsdcToSwap = usdcAmount;

    while (remainingUsdcToSwap > 0) {
        psm.fill();

        limit = dai.balanceOf(address(psm)) / psmTo18ConversionFactor;

        uint256 swapAmount = remainingUsdcToSwap < limit ? remainingUsdcToSwap : limit;

        _swapUSDCToDAI(swapAmount);

        remainingUsdcToSwap -= swapAmount;
    }
}`
