---
id: 443a2d00-b7e3-4302-8088-35c801092988
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.7
name: Check Slippage
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.7 - Check Slippage [Core]

The operator must verify the `proxy` received enough `aToken`, measured as the balance increase since the snapshot. The transaction reverts with `slippage-too-high` when the newly minted `aToken` are below `amount` scaled by `maxSlippages[aToken]`.

`        uint256 newATokens = IERC20(aToken).balanceOf(address(proxy)) - aTokenBalance;

        require(
            newATokens >= amount * maxSlippages[aToken] / 1e18,
            "MainnetController/slippage-too-high"
        );
    }`
