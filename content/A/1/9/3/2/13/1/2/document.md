---
id: 59fecdcf-6d2b-4a2d-96bf-af1729fc2bf9
docNo: A.1.9.3.2.13.1.2
name: Linear Interpolation Module Factory
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.3.2.13.1.2 - Linear Interpolation Module Factory [Core]

`lerp` instances are created using a factory contract LERP_FAB that contains standard logic for creating those instances and maintains a registry of all active `lerp` instances. The contract may also be used to cancel an existing `lerp` instance through the `remove` function. The factory contract provides a `list` method that lists the addresses of all active `lerp` instances, as well as a `tall` (short for "tick all") method that calls `tick` on all active contracts.
