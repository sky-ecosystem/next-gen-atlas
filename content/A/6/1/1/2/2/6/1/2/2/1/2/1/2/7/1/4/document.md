---
id: 5138afb5-60e9-4805-b329-254f0cd090e8
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.4
name: Resolve Pool And Snapshot Balance
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.4 - Resolve Pool And Snapshot Balance [Core]

The operator must resolve the `underlying` asset and the Aave `pool` from the `aToken`, then snapshot the `proxy` current `aToken` balance so the amount of newly minted `aToken` can be measured after the deposit.

`        IERC20    underlying = IERC20(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS());
        IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());

        uint256 aTokenBalance = IERC20(aToken).balanceOf(address(proxy));`
