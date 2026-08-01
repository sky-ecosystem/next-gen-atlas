---
id: 0ff6a176-d3c5-45c6-a55a-5fec89d3c709
docNo: A.6.1.1.2.2.6.1.2.2.1.1.2.8
name: Tokenized Treasury Owner Timelock Canceller Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.2.8 - Tokenized Treasury Owner Timelock Canceller Role [Core]

The `CANCELLER_ROLE` on the OpenZeppelin `TimelockController` holding the `OWNER_ROLE` of a Tokenized Treasury Instance is authorized to cancel queued Timelock operations before execution. The `CANCELLER_ROLE` is held by the [A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig](99bc2dd5-5573-4bb9-9210-5af299d058d9) across all Tokenized Treasury Instances, and additionally by the credit token issuer's address that holds the Timelock's `PROPOSER_ROLE`. The issuer's address is specified in each Instance Configuration Document.
