---
id: 1489f2dc-bc7b-4f73-a9e2-ba7a2e08a338
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.3
name: Read Market Tokens And Compute Minimum Output
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.3 - Read Market Tokens And Compute Minimum Output [Core]

The operator must read the market's `SY`, `PT`, and `YT` tokens, resolve the underlying `tokenOut` via `ISY(sy).yieldToken()`, and derive the expected minimum output from the current PY index using `IYT(yt).pyIndexCurrent()`. A rounding buffer of `5` is subtracted from `minTokenOut` to avoid reverts caused by potential rounding errors.

`        (address sy, address pt, address yt) = params.pendleMarket.readTokens();

        address tokenOut = ISY(sy).yieldToken();

        uint256 pyIndexCurrent = IYT(yt).pyIndexCurrent();

        uint256 minTokenOut = params.pyAmountIn * 1e18 / pyIndexCurrent - 5;`
