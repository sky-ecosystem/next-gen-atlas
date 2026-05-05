---
id: a564f010-a30f-40bb-bf36-12f91f30b8fe
docNo: A.1.9.2.4.12.3.3.11
name: Spell Validators Should Do Spell Tests And Repository Validation
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.11 - Spell Validators Should Do Spell Tests And Repository Validation [Core]

Validators should check the following:

- Ensure that all dependencies in the Spell repository (e.g., imported libraries like dss-exec-lib or git submodules) are current and up to date with the Spell. To perform this check the validator must browse or clone the GitHub repository (e.g., Spells-mainnet). Review Solidity files (e.g., in src/) for import statements, check the .gitmodules file for submodules, and run `git submodule status` to verify versions. Compare against source repositories for updates, then test with `make test` to confirm compatibility. The source repository can be identified in the Spell's source code, as the imported library or dependency is followed by "from", which points to the source path (e.g., `import {GemAbstract} from "dss-interfaces/ERC/GemAbstract.sol";` points to dss-interfaces.)
- Verify that the test scripts themselves have not been tampered with or maliciously modified in the repository.
- Confirm that the Spell repository branch matches the branch specified in the pull request or governance proposal.
