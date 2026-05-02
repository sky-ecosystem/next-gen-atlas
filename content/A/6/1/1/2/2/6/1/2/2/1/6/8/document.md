---
id: 0ff6a176-d3c5-45c6-a55a-5fec89d3c709
docNo: A.6.1.1.2.2.6.1.2.2.1.6.8
name: Tokenized Treasury Owner Timelock Canceller Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.6.8 - Tokenized Treasury Owner Timelock Canceller Role [Core]

The `CANCELLER_ROLE` on the OpenZeppelin `TimelockController` holding the `OWNER_ROLE` of a Tokenized Treasury Instance is authorized to cancel queued Timelock operations before execution. Across Tokenized Treasury Instances, this role is held by the Freezer Multisig at `0xB0113804960345fd0a245788b3423319c86940e5`.
