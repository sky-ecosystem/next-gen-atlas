---
id: 41a7e6fb-59e1-40e8-a05a-68c1520fb361
docNo: A.6.1.1.2.2.6.1.2.2.1.6.1
name: Tokenized Treasury Owner Role
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.6.1 - Tokenized Treasury Owner Role [Core]

The `OWNER_ROLE` on a Tokenized Treasury Instance is authorized to set purchase and redemption fee rates within bounds established by the `MANAGER_ADMIN_ROLE`, and to grant or revoke any role in the contract. The `OWNER_ROLE` is held by an OpenZeppelin `TimelockController` operated by the credit token issuer. The Timelock address and the holders of its `PROPOSER_ROLE` are specified in each Instance Configuration Document. The holders of the Timelock's `EXECUTOR_ROLE` and `CANCELLER_ROLE` are specified in [A.6.1.1.2.2.6.1.2.2.1.6.7 - Tokenized Treasury Owner Timelock Executor Role](35e4cd97-0d88-4a47-8fbe-487c48ecc92e) and [A.6.1.1.2.2.6.1.2.2.1.6.8 - Tokenized Treasury Owner Timelock Canceller Role](0ff6a176-d3c5-45c6-a55a-5fec89d3c709).
