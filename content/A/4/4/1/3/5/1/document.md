---
id: 5ad3e32c-9b5c-431a-bc20-e236194b65e8
docNo: A.4.4.1.3.5.1
name: Rate Setting Mechanism
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.4.4.1.3.5.1 - Rate Setting Mechanism [Core]

The SKY Borrow Rate adjusts to target a 90% utilization rate of the USDS in the stUSDS contract. When stUSDS utilization is below 90%, the rate gradually decreases; when above 90%, it gradually increases. The SKY Borrow Rate cannot fall below the SKY Borrow Minimum Rate. See [A.4.4.1.3.5.2 - SKY Borrow Minimum Rate](6e329dd6-eda5-43ce-9899-b3a03ede8d0b).

The specific parameters and formula governing the rate of adjustment are specified in the documents herein.
