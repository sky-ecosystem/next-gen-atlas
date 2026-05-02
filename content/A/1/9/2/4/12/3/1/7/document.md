---
id: 7f3112c8-ed90-4dfc-b29a-eae1d3492a11
docNo: A.1.9.2.4.12.3.1.7
name: Spell Validators Must Check Deployed Spell Optimization Settings
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.7 - Spell Validators Must Check Deployed Spell Optimization Settings [Core]

Validators must ensure that the code optimization settings used by the Spell contract are correct.
Validators should ensure the following:

- The `Optimization Enabled` field on Etherscan is set to `No with 200 runs` unless explicitly required due to contract size constraints during deployment.
- If optimization is enabled, the value of the `Optimization Enabled` must be `Yes with 200 runs` unless the optimization settings have been specified in the Instruction Document as a specific number of runs, which must be a multiple of 100 other than 0.
- If the optimization settings are incorrect (e.g., `No with 13767 runs` or `Yes with 0 runs`), the Spell fails validation.

To perform this validation, the validator must go to the contract tab on Etherscan and review the `Optimization Enabled` field under the contract’s metadata.
