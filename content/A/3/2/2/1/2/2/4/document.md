---
id: 227eff62-f2aa-4e49-91ad-1321261ed299
docNo: A.3.2.2.1.2.2.4
name: Lindy Adjustment Factor
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2.4 - Lindy Adjustment Factor [Core]

The Lindy Adjustment Factor $\text{LAF}$ is a measure of the "Lindiness" of the smart contracts and is based on the idea that vulnerable smart contracts with large TVL for a significant period of time would have already been hacked. Therefore, protocols with a greater time integrated TVL are safer, all other things equal, than protocols with a lower time integrated TVL. The $\text{LAF}$ is calculated as follows:

$$
\text{LAF} = max(0, 1 - \frac{ln(1 + \lambda \times \text{AGEeff})}{ln(1 + \lambda \times \text{max})})
$$

Here $max$ is the mathematical maximum function that returns the greater of the specified parameters and $ln$ is the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.
