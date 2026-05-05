---
id: 2407adac-7204-4dbe-acb8-abde6e0e57e9
docNo: A.1.9.2.4.12.3.1.3
name: Spell Validators Must Validate DssExecLib Library
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.3 - Spell Validators Must Validate DssExecLib Library [Core]

Validators must ensure that the address of the `DssExecLib` library is correct. The correct address corresponds to the latest release as specified in the `DssExecLib` GitHub repository. The deployed Spell must use and display the correct `DssExecLib` address on Etherscan to pass validation.

The validation can be performed by navigating to the "Libraries Used" section on the "Contract tab" on Etherscan. The library address displayed there must be compared against the official address specified in the README file ([https://github.com/sky-ecosystem/dss-exec-lib?tab=readme-ov-file#dss-exec-library](https://github.com/sky-ecosystem/dss-exec-lib?tab=readme-ov-file#dss-exec-library)) of the `DssExecLib` GitHub repository.
