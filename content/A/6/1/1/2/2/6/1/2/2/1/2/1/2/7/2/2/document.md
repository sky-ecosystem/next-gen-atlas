---
id: dbadb917-8810-4515-84da-c68c6a6002a3
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.2
name: Resolve Aave Pool
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.2 - Resolve Aave Pool [Core]

The operator must resolve the Aave `pool` from the `aToken` in order to withdraw the underlying asset.

`        IAavePool pool = IAavePool(IATokenWithPool(aToken).POOL());`
