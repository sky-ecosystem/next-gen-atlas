---
id: 955c8db9-7bd7-4e49-b23c-7b482c84ca97
docNo: A.6.1.1.2.2.6.1.2.2.1.1.1.3
name: ALM Controller Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.1.3 - ALM Controller Role [Core]

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role. This role applies to the monolithic ALM Controller implementation; the equivalent role for the Diamond PAU implementation is specified in [A.6.1.1.2.2.6.1.2.2.1.1.3.2 - Controller Role](1597253b-b936-46f6-98c7-d41d4306d2c5).
