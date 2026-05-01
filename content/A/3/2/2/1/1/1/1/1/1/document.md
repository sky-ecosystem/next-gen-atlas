---
id: 6766c25f-3e67-41e0-8b66-5af444c40572
docNo: A.3.2.2.1.1.1.1.1.1
name: Calculate Probability Of Default
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.3.2.2.1.1.1.1.1.1 - Calculate Probability Of Default [Core]

The first step is calculating the Probability Of Default $PD$. $PD$ is calculated using the following formula:

$$
\text{PD} = N(-d_1) + N(-d_2) \left( \frac{\sum_{i=1}^n \text{LT}_i V_0^i}{\sum_{j=1}^m D_0^j} \right)^{-2a}
$$

Here $N$ is the normal cumulative probability distribution function.

The parameters of this formula are specified in the subdocuments herein.
