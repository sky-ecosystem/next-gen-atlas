---
id: 0082c12d-f1a7-46ff-a4aa-5fe42ece1a4d
docNo: A.3.3.2.1.1
name: Peg Stability Module
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.3.3.2.1.1 - Peg Stability Module [Core]

A Peg Stability Module ("PSM") allows users to swap a given collateral type directly for Dai or USDS at a fixed rate, rather than borrowing Dai or USDS. The PSM contract was designed with Stablecoin collateral in mind, allowing users to swap other Stablecoins for Dai or USDS at a fixed rate to aid with keeping Dai or USDS pegged to one (1) USD.

A PSM operates similarly to a regular vault type with a zero Stability Fee and a liquidation ratio of 100% that can only be accessed through a user-facing smart contract containing the relevant swap functions. Unlike regular vaults, users of the PSM do not retain ownership of the asset and borrow Dai or USDS. Instead, PSM users swap the asset directly for Dai or USDS.
