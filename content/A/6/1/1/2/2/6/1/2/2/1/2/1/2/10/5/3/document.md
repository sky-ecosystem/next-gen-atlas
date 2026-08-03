---
id: 3b6f10ae-e696-4c3c-9097-e9a9e7765dec
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.3
name: Cooldown Assets On sUSDe
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.3 - Cooldown Assets On sUSDe [Core]

The operator must call the `MainnetController` contract to `cooldownAssets` on `susde` for the `usdeAmount`. The call is executed against the sUSDe vault through `proxy.doCall`, starting the cooldown period after which the specified `usdeAmount` of USDe can be unstaked to the Grove ALM Proxy.

`        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.cooldownAssets, (usdeAmount))
        );
    }`
