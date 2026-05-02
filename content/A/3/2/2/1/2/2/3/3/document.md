---
id: ce3f2e96-b643-4de7-bfb9-cb0aee678635
docNo: A.3.2.2.1.2.2.3.3
name: Raw Code Complexity Rating
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2.3.3 - Raw Code Complexity Rating [Core]

The Raw Code Complexity Rating $\text{RawCCR}$ is an unnormalized measure of the complexity of the code of the smart contracts that implement the protocol. The $\text{RawCCR}$ is calculated as follows:

$$
\text{RawCCR}=(\text{TCC} \times \text{CCweight}) + (\text{TDP} \times \text{DPweight}) + (\text{TEC} \times \text{ECweight}) + (\text{ID} \times \text{IDweight}) + (\frac{\text{CS}}{\text{CSfactor}} \times \text{CSweight})
$$

The parameters of this formula are specified in the subdocuments herein.
