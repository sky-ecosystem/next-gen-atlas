---
id: eb5de4dd-2921-439e-bbce-a26f66410c48
docNo: A.2.11.1.3.2.2.2.2.2.1
name: Transaction Hash Verification
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.11.1.3.2.2.2.2.2.1 - Transaction Hash Verification [Core]

Signers must verify that the transaction hash displayed on the signing device matches the expected transaction hash derived from the transaction parameters. When signing transactions involving nested Multisigs, the hash displayed on the signing device may correspond to an approval hash rather than the underlying transaction. In such cases, signers must verify both the nested transaction and the parent Multisig approval.
