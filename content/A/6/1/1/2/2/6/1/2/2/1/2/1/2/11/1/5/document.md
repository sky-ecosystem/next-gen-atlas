---
id: 3b8311b9-a8db-45a0-9fd3-84970c0eb246
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.5
name: Redeem PT To Token
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.5 - Redeem PT To Token [Core]

The operator must redeem the principal tokens for the underlying `tokenOut` by calling `redeemPyToToken` on the `PENDLE_ROUTER` through the `proxy`, sending the proceeds to the `proxy`.

`        params.proxy.doCall(
            params.pendleRouter,
            abi.encodeCall(
                IPendleRouter.redeemPyToToken, (
                    address(params.proxy),
                    yt,
                    params.pyAmountIn,
                    createSimpleTokenOutput(tokenOut, minTokenOut)
                )
            )
        );`
