---
id: 35ce6b38-9fc1-456e-93da-10ab1468a8bf
docNo: A.3.3.2.2.1.2.1
name: Latent Actively Stabilizing Collateral Calculations
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.3.2.2.1.2.1 - Latent Actively Stabilizing Collateral Calculations [Core]

Latent Actively Stabilizing Collateral is currently calculated as the sum of:

1. Cash Stablecoins in Curve (not paired with USDS);
2. Cash Stablecoins in Uniswap (not paired with USDS);
3. Cash Stablecoins in SparkLend;
4. Cash Stablecoins in Aave;
5. Cash Stablecoins in Morpho; and
6. Cash Stablecoins in a Prime ALM Proxy.

The Core Executor Agents, in consultation with the Core Council Risk Advisor, may impose limitations on the size of exposures to these protocols or to specific pools within these protocols that qualify as Latent Actively Stabilizing Collateral in order to prevent excessive risk to Sky.
