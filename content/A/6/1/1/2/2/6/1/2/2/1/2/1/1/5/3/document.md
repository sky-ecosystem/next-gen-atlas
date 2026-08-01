---
id: 153007a4-f8ac-460b-984e-bc736def634c
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.3
name: Set The Lower Tick Bound
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.3 - Set The Lower Tick Bound [Core]

The operator must set the pool's lower `addLiquidityTickBounds` to the supplied `lowerTickBound`, which constrains the lower end of the price range used when adding liquidity to the `pool`.

`
        params.addLiquidityTickBounds.lower = lowerTickBound;`
