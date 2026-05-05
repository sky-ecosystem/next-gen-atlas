---
id: a8db99b2-f072-4132-9ee2-c8ebcc2b3609
docNo: A.3.2.2.1.2.2.4.3
name: Effective Age
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2.4.3 - Effective Age [Core]

The Effective Age $\text{AGEeff}$ is the age of the contracts adjusted for the TVL of the contracts. The $\text{AGEeff}$ is calculated as follows:

$$
\text{AGEeff}=\text{CA} \times ln(1 + \frac{\text{gmTVL}}{\text{TVLthreshold}})
$$

Here $ln$ is the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.
