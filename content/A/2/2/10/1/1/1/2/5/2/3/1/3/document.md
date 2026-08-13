---
id: 8d3420d5-86a7-4468-8f08-92cc00fed557
docNo: A.2.2.10.1.1.1.2.5.2.3.1.3
name: Deposit Asset Into Basin
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.2.2.10.1.1.1.2.5.2.3.1.3 - Deposit Asset Into Basin [Core]

The Basin Facet's `deposit` function deposits the specified amount of the asset into the Basin on behalf of the ALM Proxy, and Basin shares are minted to the ALM Proxy. The deposit does not complete unless the number of shares minted is at least the specified minimum (`minSharesOut`).
