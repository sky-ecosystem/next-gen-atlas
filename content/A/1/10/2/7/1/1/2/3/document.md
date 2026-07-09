---
id: 2c825419-d9a7-4da7-97b8-29e2c8b515a4
docNo: A.1.10.2.7.1.1.2.3
name: Initialization Script Requirements
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.10.2.7.1.1.2.3 - Initialization Script Requirements [Core]

Initialization scripts must satisfy the following requirements:

- The initialization library must be directly importable by a compliant Spell without modifications. The execution context of the library is expected to be the relevant Governance proxy.
- Every initialization function must be audited.
- Top-level initialization scripts that exist solely for test environments must not be included in the audit scope.
