---
id: 7ccfae3d-59ae-433e-adba-7822ae335755
docNo: A.3.2.2.1.2.2.5.2
name: Decay Factor
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.2.5.2 - Decay Factor [Core]

The Decay Factor $decayFactor$ is a parameter indicating how rapidly the effectiveness of audits in reducing risk decreases over time. The $decayFactor$ is calculated as follows:

$$
decayFactor =\begin{cases}1 & \text{if } auditAge \leq 2 \\\frac{10 - auditAge}{8} & \text{if } 2 < auditAge < 10 \\0 & \text{if } auditAge \geq 10\end{cases}
$$

The parameter of this formula is specified in the subdocument herein.
