---
id: 3cbd5aaf-8ff5-4009-884a-71d776c3769a
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `redeemPendlePT`; the function calls `_checkRole(RELAYER)` before delegating the redemption logic to `PendleLib`.

`function redeemPendlePT(address pendleMarket, uint256 pyAmountIn, uint256 minAmountOut)
        external`
