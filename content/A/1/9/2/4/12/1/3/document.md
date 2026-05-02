---
id: 101d5bee-6ba8-449e-9bb0-cc31bc929390
docNo: A.1.9.2.4.12.1.3
name: Ecosystem Spell Verification Scope
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.1.3 - Ecosystem Spell Verification Scope [Core]

The scope of Spell validation includes any code in the Sky Protocol that:

1. Must adhere to the `GSM Pause Delay` enforced by the Sky Protocol’s `ds-pause` contract, and
2. Is directly executed by the Sky Protocol’s `Pause Proxy` contract.

Actions that do not meet these criteria—such as `instant actions`, `MOM` and `IAM` contract calls—are excluded from Spell validation.

This exclusion is due to the absence of a pause delay for such actions, which prevents ecosystem actors from having sufficient time to perform their reviews.

Validators should also consider validating the source code or associated audits for contracts added to the Chainlog as part of a Spell, even if these contracts are not immediately executed or fall outside the standard validation scope. This includes pre-deployed emergency Spell contracts, ensuring that their integrity and security are assessed at the time of addition to the Chainlog for potential future use.
