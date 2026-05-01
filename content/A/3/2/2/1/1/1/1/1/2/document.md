---
id: c9bd4928-d054-4e89-9a98-720c439b0db3
docNo: A.3.2.2.1.1.1.1.1.2
name: Calculate Loss Given Default
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.3.2.2.1.1.1.1.1.2 - Calculate Loss Given Default [Core]

The second step is calculating the Loss Given Default $LGD$. $LGD$ is calculated using the following formula:

$$
LGD = min(1 - \frac{(1 - LP) * (1 - S)}{LT}, 0)
$$

Here $min$ is the mathematical minimum function that returns the lower of the two specified parameters.

The parameters of this formula are specified in the subdocuments herein. All of these parameters should be specified as decimal numbers. For example, 3% should be specified as `0.03`.
