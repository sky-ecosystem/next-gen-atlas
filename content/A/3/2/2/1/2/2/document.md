---
id: 00fd9362-f606-49bc-a425-9c96008be238
docNo: A.3.2.2.1.2.2
name: Smart Contract Risk Rating Calculation
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2 - Smart Contract Risk Rating Calculation [Core]

The second step in calculating the Instance Smart Contract RRC with respect to an Allocation System opportunity is to calculate the Smart Contract Risk Rating $SCRR$ for the covered smart contracts identified in [A.3.2.2.1.2.1 - Defining Relevant Smart Contracts](162cfc93-77bd-4878-a8be-370d8862d792). The $SCRR$ is calculated as follows:

$$
\text{SCRR} = min[\text{CAP}, (\text{SR} + \text{CCR}) \times \text{LAF} \times {AF}]
$$

Here $min$ is the mathematical minimum function that returns the lesser of the specified parameters.
The parameters of this formula are specified in the subdocuments herein.
