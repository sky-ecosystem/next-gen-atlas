---
id: 3ad29e6a-90fb-4739-aacf-434e467c070e
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.1
name: Relayer Role
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawERC4626` tokens. Also, they must ensure the contract `isActive` i.e. can process the request.

`function withdrawERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        isActive`
