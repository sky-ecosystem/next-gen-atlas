---
id: 7e85c9ff-3548-4a98-8d86-71b6fae340d8
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownSharesSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function cooldownSharesSUSDe(uint256 susdeAmount)
        external
        returns (uint256 cooldownAmount)
    {
        _checkRole(RELAYER);`
