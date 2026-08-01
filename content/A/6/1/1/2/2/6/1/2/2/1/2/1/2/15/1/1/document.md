---
id: f0f317d1-5c78-4de8-956e-dba3a3256eff
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferUSDCToCCTP`.

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain) external {
        _checkRole(RELAYER);`
