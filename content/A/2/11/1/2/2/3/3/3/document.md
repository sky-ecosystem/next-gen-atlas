---
id: c6591c5c-c767-4769-b2d6-80564d96fa48
docNo: A.2.11.1.2.2.3.3.3
name: Accounts
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.11.1.2.2.3.3.3 - Accounts [Core]

The `accounts` parameter for each chain is a list of contracts to be included in Safe Harbor. Each contract listed must include the sub-elements of (1) the `accountAddress` of the contract and (2) the `childContractScope`, which specifies whether child contracts of the specified contract are covered. The possible values for the `childContractScope` parameter are: (1) `None` (no child contracts are in scope), (2) `ExistingOnly` (only child contracts created prior to calling `adoptSafeHarbor` are in scope), or (3) `All` (all child contracts are in scope).

The value of the `scope` parameter is all contracts specified in the Bug Bounty Program.

The `childContractScope` parameter for each contract is specified in the Bug Bounty Program.
