---
id: 3f441562-4c03-429c-8934-f0f87fa0eee7
docNo: A.2.11.1.3.2.1.2.2
name: Signer Security Requirements
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.11.1.3.2.1.2.2 - Signer Security Requirements [Core]

Multisig signers must comply with the following security requirements:

- All Multisig signers must use hardware wallets for signing operations. The associated seed phrase must be securely backed up using physical, offline storage methods only. Seed phrases must never be stored digitally, including in photographs, files, password managers, cloud storage, email, or messaging applications. Seed phrase backups must be stored on durable offline media and kept in secure physical locations with appropriate access controls to prevent unauthorized access or single-point compromise.
- Signers must use a unique signing address per Multisig and must not reuse the same signing address across Multisigs.
- Signers participating in Multisigs responsible for critical protocol configuration or security-sensitive operations should not use their signing addresses for personal transactions or other unrelated activities and should instead use a dedicated address created specifically for Multisig participation.
