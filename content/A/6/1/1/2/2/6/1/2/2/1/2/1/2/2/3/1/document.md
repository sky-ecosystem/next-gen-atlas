---
id: 73d565c3-561c-4b54-a491-0fa2257bf9dd
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `redeemERC4626`. Unlike deposits and withdrawals, this operation applies its rate limit after redemption rather than before, since the resulting assets are not known until the shares are redeemed.

`function redeemERC4626(address token, uint256 shares)
        external
        onlyRole(RELAYER)
        returns (uint256 assets)`
