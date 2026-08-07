---
id: 9f28cd92-e805-4579-a509-69e01db491f2
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.5
name: Approve Aave Pool Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.5 - Approve Aave Pool Spend [Core]

The operator must approve the Aave `pool` to spend the `amount` of `underlying` on behalf of the `proxy`, which assumes the `proxy` holds enough of the `underlying` asset.

`        // Approve underlying to Aave pool from the proxy (assumes the proxy has enough underlying).
        ERC20Lib.approve(proxy, address(underlying), address(pool), amount);`
