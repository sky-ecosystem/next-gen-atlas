---
id: 1224be29-4148-4720-919d-8d15d519763d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.2 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for transferring the required `amount`. The rate limit is keyed on the `oftAddress` and `destinationEndpointId` pair through `LIMIT_LAYERZERO_TRANSFER`. Note that this function was deployed without integration testing, so its rate limit must be kept at `0` until the LayerZero dependencies are live and the functionality has been thoroughly integration tested.

`        _rateLimited(
            keccak256(abi.encode(LIMIT_LAYERZERO_TRANSFER, oftAddress, destinationEndpointId)),
            amount
        );`
