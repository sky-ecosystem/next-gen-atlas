---
id: 8bde4dd3-aead-466e-ae9f-49dc8dcf8457
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.3
name: Check Pool Coin Count
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.3 - Check Pool Coin Count [Core]

The operator must ensure both `inputIndex` and `outputIndex` are less than the pool's `N_COINS`, otherwise the call reverts with `CurveLib/index-too-high`.

`ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        uint256 numCoins = curvePool.N_COINS();
        require(
            params.inputIndex < numCoins && params.outputIndex < numCoins,
            "CurveLib/index-too-high"
        );`
