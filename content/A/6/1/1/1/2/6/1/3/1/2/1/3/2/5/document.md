---
id: 9349014e-68e7-4832-bbab-d0d9fa34607b
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.5
name: Retrieve Aave Address
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.5 - Retrieve Aave Address [Core]

The operator must retrieve the Aave pool contract address associated with the given `aToken`. This address represents the Aave lending pool from which the assets are withdrawn.

    `IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());`
