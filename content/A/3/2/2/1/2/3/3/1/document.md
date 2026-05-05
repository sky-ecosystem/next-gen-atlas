---
id: 7441253c-0030-4b8e-ac91-65046761aab6
docNo: A.3.2.2.1.2.3.3.1
name: Piecewise Function
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.2.2.1.2.3.3.1 - Piecewise Function [Core]

The Piecewise Function $CRR(x)$ calculates a percentage risk capital requirement based on an input $x$ and is defined as follows:

$$
\text{CRR}(x) =\begin{cases}a & \text{if } x \le x_{\text{start}}, \\[8pt]b \times \dfrac{x - x_{\text{start}}}{x_{\text{kink}} - x_{\text{start}}} & \text{if } x_{\text{start}} < x \le x_{\text{kink}}, \\[8pt]b \;+\; c \;\dfrac{x - x_{\text{kink}}}{x_{\text{max}} - x_{\text{kink}}}& \text{if } x_{\text{kink}} < x < x_{\text{max}}, \\[8pt]d& \text{if } x \ge x_{\text{max}}.\end{cases}
$$
