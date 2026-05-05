---
id: 152bc5d8-7642-424c-b5fc-9242479f705e
docNo: A.3.2.2.1.1.1.1.1.4
name: Calculate Capital Requirement Without Buffers
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.3.2.2.1.1.1.1.1.4 - Calculate Capital Requirement Without Buffers [Core]

The fourth step is to calculate the Capital Requirement Without Buffers $K$. $K$ is calculated as follows:

$$
K = \left[ LGD \times N\left( \frac{N^{-1}(PD) + \sqrt{R} \cdot N^{-1}(0.999)}{\sqrt{1-R}} \right) - PD \times LGD \right]
$$

Here $N$ is the cumulative normal probability distribution function and $N^{-1}$ is the inverse cumulative normal probability distribution function.
