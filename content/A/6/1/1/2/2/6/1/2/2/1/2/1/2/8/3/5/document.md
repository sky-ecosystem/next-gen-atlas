---
id: 44e41f28-d634-460b-b084-1c3a356a355e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.5
name: Remove Liquidity
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.5 - Remove Liquidity [Core]

The operator must call `remove_liquidity` on the `pool` through the `proxy`, burning `lpBurnAmount` LP shares and returning the withdrawn tokens to the `proxy`.

`withdrawnTokens = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.remove_liquidity,
                    (params.lpBurnAmount, params.minWithdrawAmounts, address(params.proxy), false)
                )
            ),
            (uint256[])
        );`
