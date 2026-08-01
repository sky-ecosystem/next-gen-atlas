---
id: 5bbe99a6-c616-4857-a220-7f2f0bd0ac0d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.6
name: Clear Dust Approvals
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.6 - Clear Dust Approvals [Core]

The operator must ensure that the liquidity added is not zero, then reset the `positionManager` allowance for both tokens back to zero to clear any dust approval.

`require(liquidity != 0, "UniswapV3Lib/no-liquidity-increased");

        // Clear approvals of dust
        ERC20Lib.approve(context.proxy, token0, address(params.positionManager), 0);
        ERC20Lib.approve(context.proxy, token1, address(params.positionManager), 0);`
