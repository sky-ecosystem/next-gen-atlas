---
id: bbf43294-09c2-413a-b0a4-745cb72d1cd8
docNo: A.3.2.2.1.1.1.1.1.3
name: Calculate Asset Correlation Coefficient
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.3.2.2.1.1.1.1.1.3 - Calculate Asset Correlation Coefficient [Core]

The third step is to calculate the Asset Correlation Coefficient $R$. $R$ is calculated as follows:

$$
R = a \times \left(1 - e^{-K \times PD}\right) + b \times \left(1 - \left(1 - e^{-K \times PD}\right)\right)
$$

Here $e$ is the base of the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.
