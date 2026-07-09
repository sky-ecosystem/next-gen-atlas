---
id: 35e4cd97-0d88-4a47-8fbe-487c48ecc92e
docNo: A.6.1.1.2.2.6.1.2.2.1.1.2.7
name: Tokenized Treasury Owner Timelock Executor Role
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.1.2.7 - Tokenized Treasury Owner Timelock Executor Role [Core]

The `EXECUTOR_ROLE` on the OpenZeppelin `TimelockController` holding the `OWNER_ROLE` of a Tokenized Treasury Instance is authorized to execute queued operations once the Timelock delay period has elapsed. Across Tokenized Treasury Instances, this role is held by the Grove [A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account](d143241d-5819-432d-a6ba-892961502838).
