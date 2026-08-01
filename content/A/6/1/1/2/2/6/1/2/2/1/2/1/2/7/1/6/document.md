---
id: 028a06d5-c91d-42ff-8a0d-a6f272948d90
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.6
name: Supply To Aave Pool
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.6 - Supply To Aave Pool [Core]

The operator must `supply` the `underlying` into the Aave `pool` on behalf of the `proxy`, so that the `proxy` receives the corresponding `aToken`.

`        // Deposit underlying into Aave pool, proxy receives aTokens
        proxy.doCall(
            address(pool),
            abi.encodeCall(pool.supply, (address(underlying), amount, address(proxy), 0))
        );`
