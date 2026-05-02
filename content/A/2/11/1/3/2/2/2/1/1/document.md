---
id: c6bcbd5f-7450-4c6e-9aa6-82c49a678bd3
docNo: A.2.11.1.3.2.2.2.1.1
name: Signer Address Update Process If Original Key Is Accessible
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.11.1.3.2.2.2.1.1 - Signer Address Update Process If Original Key Is Accessible [Core]

If the original key of the signer address that needs to be changed remains accessible, the following steps must be completed by the signer:

- The signer authorizes the address change by signing a message with the existing signer address. The signed message must clearly state the intent to replace the existing signer address with the new address.
- The signer must follow the steps defined in [A.2.11.1.3.2.1.2.1 - Signer Verification Process](002821ab-c67c-4eb1-987c-69e759ab7b3c) prior to the new address being added to the Multisig.
