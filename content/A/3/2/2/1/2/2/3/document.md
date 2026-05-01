---
id: 295e4d3b-8c8a-4f74-879f-88060bb07803
docNo: A.3.2.2.1.2.2.3
name: Code Complexity Rating
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2.3 - Code Complexity Rating [Core]

The Code Complexity Rate $CCR$ is a measure of the complexity of the code of the smart contracts used by the protocol. The $CCR$ is calculated as follows:

$$
CCR = \text{CCRMax} \times min(1, \frac{\text{RawCCR} + 1}{\text{CCRUpperBound} + 1})
$$

Here the $min$ function is the mathematical minimum function that returns the lesser of the specified parameters.

The parameters of this formula are specified in the subdocuments herein.
