---
id: 49603674-9276-4588-9855-e45fbd67b57b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawAave`, which is enforced by the `_checkRole` check at the start of the function.

`function withdrawAave(address aToken, uint256 amount)
        external
        returns (uint256 amountWithdrawn)
    {
        _checkRole(RELAYER);`
