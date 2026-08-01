---
id: bd3ff49e-77af-4757-984d-f8e91346e702
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `swapUSDSToUSDC`, which the controller enforces with `onlyRole(RELAYER)` before delegating the swap to `PSMLib.swapUSDSToUSDC`.

`function swapUSDSToUSDC(uint256 usdcAmount)
        external
        onlyRole(RELAYER)`
