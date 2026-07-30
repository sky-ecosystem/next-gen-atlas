---
id: 31251f84-cfab-483f-b98c-9cf72f2c348b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `requestRedeemERC7540`.

`function requestRedeemERC7540(address token, uint256 shares) external {
        _checkRole(RELAYER);`
