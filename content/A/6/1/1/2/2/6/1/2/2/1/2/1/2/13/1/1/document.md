---
id: 123fc395-d16c-431e-8d09-8bbd78b0e405
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferTokenLayerZero`. The function is `payable` so that the operator can supply the native gas required to pay the LayerZero messaging fee.

`    function transferTokenLayerZero(
        address oftAddress,
        uint256 amount,
        uint32  destinationEndpointId
    )
        external payable
    {
        _checkRole(RELAYER);`
