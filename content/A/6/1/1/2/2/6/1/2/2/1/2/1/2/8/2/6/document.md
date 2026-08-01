---
id: 3b14adbf-eb29-4ae2-ae3c-3366ae7db9ce
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.6
name: Add Liquidity
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.6 - Add Liquidity [Core]

The operator must call `add_liquidity` on the `pool` through the `proxy`, depositing the tokens and returning the minted LP `shares` to the `proxy`.

`shares = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.add_liquidity,
                    (params.depositAmounts, params.minLpAmount, address(params.proxy))
                )
            ),
            (uint256)
        );`
