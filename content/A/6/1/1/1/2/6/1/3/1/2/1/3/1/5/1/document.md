---
id: 5b405222-e981-44b7-853b-09d1976fdbbb
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.5.1
name: Retrieve Aave Address
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.5.1 - Retrieve Aave Address [Core]

The operator must retrieve the Aave pool contract address associated with the given `aToken`. This address represents the Aave lending pool where the assets are deposited. `IAavePool` interface allows interaction with the Aave pool's functions (like `supply`).

`    IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());`
