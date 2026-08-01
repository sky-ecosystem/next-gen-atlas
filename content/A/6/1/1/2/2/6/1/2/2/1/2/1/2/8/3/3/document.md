---
id: 43167a40-dcb7-4b17-a615-1e359771822d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.3
name: Aggregate Minimum Withdrawal Value
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.3 - Aggregate Minimum Withdrawal Value [Core]

The operator must aggregate the minimum value to be withdrawn from `minWithdrawAmounts` using the pool's `stored_rates`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 valueMinWithdrawn;
        for (uint256 i = 0; i < params.minWithdrawAmounts.length; i++) {
            valueMinWithdrawn += params.minWithdrawAmounts[i] * rates[i];
        }
        valueMinWithdrawn /= 1e18;`
