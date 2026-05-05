---
id: 60767684-f67f-4e03-85db-7718af41b827
docNo: A.1.9.3.2.13
name: Linear Interpolation Module
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.13 - Linear Interpolation Module [Core]

The Linear Interpolation Module (`lerp`) is a smart contract tool that allows a governance parameter to be adjusted on a straight-line basis over time, without requiring additional Executive Votes. The Linear Interpolation Module refers to the smart contract logic that enables time-based parameter changes. To deploy individual `lerp` instances, each of which manages the adjustment of a specific parameter over time, the Linear Interpolation Module Factory contract is used. Once authorized through an Executive Vote, the `lerp` may enact parameter changes without being subject to the GSM Pause Delay. The subdocuments herein specify the features of the `lerp` and its authorized use.
