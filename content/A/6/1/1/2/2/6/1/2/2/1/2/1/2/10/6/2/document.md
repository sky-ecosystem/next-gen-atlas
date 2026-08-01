---
id: 11f21172-0294-4c61-8234-562b63aa5681
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.2
name: Cooldown Shares On sUSDe
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.2 - Cooldown Shares On sUSDe [Core]

The operator must call the `MainnetController` contract to `cooldownShares` on `susde` for the `susdeAmount`. The call is executed against the sUSDe vault through `proxy.doCall`, and the returned `cooldownAmount` of USDe assets is decoded from the result.

`        cooldownAmount = abi.decode(
            proxy.doCall(
                address(susde),
                abi.encodeCall(susde.cooldownShares, (susdeAmount))
            ),
            (uint256)
        );`
