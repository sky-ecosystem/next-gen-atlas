---
id: 71776219-5425-4eaf-89fe-7dea283d5a7d
docNo: A.3.3.2.7.1.1.1.6
name: Lite Peg Stability Module Buffer Definition
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.3.3.2.7.1.1.1.6 - Lite Peg Stability Module Buffer Definition [Core]

`buf` is a fixed-sized amount of pre-minted Dai which LitePSM is designed to maintain in most situations. Note, however, that when a user calls `buyGem`, the amount of Dai available can be temporarily larger than `buf`.
