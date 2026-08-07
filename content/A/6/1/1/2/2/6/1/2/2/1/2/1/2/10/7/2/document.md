---
id: da4abe97-3014-4a48-ad17-7beb0e12b451
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.2
name: Unstake To ALM Proxy
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.2 - Unstake To ALM Proxy [Core]

The operator must call the `MainnetController` contract to `unstake` from `susde` to the `proxy`. The call is executed against the sUSDe vault through `proxy.doCall`, withdrawing the USDe assets to the Grove ALM Proxy once the cooldown period has elapsed.

`        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.unstake, (address(proxy)))
        );
    }`
