---
id: 14e225e3-5667-49bb-9773-7cb58cd32874
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.3
name: Approve And Aggregate Deposit Value
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.3 - Approve And Aggregate Deposit Value [Core]

The operator must approve the `pool` to spend each deposited token on behalf of the `proxy` and aggregate the total value deposited using the pool's `stored_rates`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 valueDeposited;
        for (uint256 i = 0; i < params.depositAmounts.length; i++) {
            ERC20Lib.approve(params.proxy, curvePool.coins(i), params.pool, params.depositAmounts[i]);
            valueDeposited += params.depositAmounts[i] * rates[i];
        }
        valueDeposited /= 1e18;`
