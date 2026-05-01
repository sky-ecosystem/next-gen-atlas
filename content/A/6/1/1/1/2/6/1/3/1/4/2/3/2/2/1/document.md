---
id: e2e16365-4a11-4df4-ab33-332fd9a14fac
docNo: A.6.1.1.1.2.6.1.3.1.4.2.3.2.2.1
name: Decode For Underlying Shares
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.2.1 - Decode For Underlying Shares [Core]

The operator must decode the result returned by the `cooldownShares` function into a `uint256` value, representing the amount of shares that were actually cooled down (`cooldownAmount`).

`{
    cooldownAmount = abi.decode(
        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.cooldownShares, (susdeAmount))
        ),
        (uint256)
    );`
