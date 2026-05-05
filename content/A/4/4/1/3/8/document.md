---
id: 37f8f82e-7239-4cfb-8f95-d2cc40515cd9
docNo: A.4.4.1.3.8
name: stUSDS Bounded External Access Module
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.4.4.1.3.8 - stUSDS Bounded External Access Module [Core]

The stUSDS Bounded External Access Module (stUSDS BEAM) enables designated, Governance-whitelisted operators to adjust the stUSDS Rate (`str`), the SKY Borrow Rate (`duty`), the maximum amount that users can deposit into the stUSDS contract (`cap`), and the maximum Debt Ceiling (`line`). Adjustments are governed by the stUSDS BEAM smart contract logic and specific parameters set by Sky Governance. stUSDS BEAM holds four parameters that can be set for each stUSDS parameter: (i) `min`, (ii) `max`, (iii) `step`, and (iv) `tau`.
