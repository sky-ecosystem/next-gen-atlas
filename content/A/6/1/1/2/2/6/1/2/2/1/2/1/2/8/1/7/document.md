---
id: 39d942fe-5c37-4950-bc50-d898c0a5f997
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.7
name: Execute Swap
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.7 - Execute Swap [Core]

The operator must call `exchange` on the `pool` through the `proxy`, swapping the input token for the output token and returning the received `amountOut` to the `proxy`.

`amountOut = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.exchange,
                    (
                        int128(int256(params.inputIndex)),
                        int128(int256(params.outputIndex)),
                        params.amountIn,
                        params.minAmountOut,
                        address(params.proxy)
                    )
                )
            ),
            (uint256)
        );
    }`
