---
id: 4f7f2b2f-3514-4ba6-a1a2-6dd40fff5a92
docNo: A.1.9.2.4.12.3.3.5
name: Spell Validators Should Review Chainlog
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.5 - Spell Validators Should Review Chainlog [Core]

Spell validators should ensure that all `DssExecLib` calls to the chainlog use the correct name descriptors.

- Verify that all Chainlog references, such as name descriptors or keys, correspond to valid, existing entries in the Chainlog.
- Confirm that the name descriptors match the expected values as recorded in the Chainlog.
- The chainlog patch version is updated correctly (e.g., `x.y.z` → `x.y.z+1`).

To perform this validation the validators must go to the "Contract" tab on Etherscan and review the source code. Look for `DssExecLib` calls in the code. Compare the name descriptors in the code with the expected values in the Chainlog.
