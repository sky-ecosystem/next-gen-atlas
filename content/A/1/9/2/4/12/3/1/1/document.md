---
id: ea1d866c-41ed-474b-91ce-d9f6428bc158
docNo: A.1.9.2.4.12.3.1.1
name: Spell Validators Must Ensure Tests Pass
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.1 - Spell Validators Must Ensure Tests Pass [Core]

Ecosystem Spell validators must execute the predefined tests associated with a Spell. These tests are provided as scripts in the Spell repository on GitHub. Validators must run these scripts to verify the correctness, security, and compatibility of the Spell. All tests must pass successfully—without errors or failures—for the Spell to pass validation.

The best practice for running the tests are specified herein:

1. If you haven’t cloned the repository before, run: `git clone <https://github.com/sky-ecosystem/Spells-mainnet`>.
2. Navigate to the Spell repository directory by running: `cd Spells-mainnet`.
3. Update the repository for the latest changes by running: `git pull`.
4. Switch to the correct branch by finding the name from the Spell’s pull request on GitHub, run the command: `git checkout NAME`.
5. Verify your setup and check that you’re on the correct branch by running: `git status`.
6. Clean up old Spell library dependencies by running the command: `rm -r lib` or deleting the `lib` folder and its contents.
7. Install libraries required for the current Spell by running `git submodule update --init --recursive`.
8. Configure the local or remote node being used by running `export ETH_RPC_URL=URL` with the URL of your local or remote node. If using a remote node, do not share the URL as it can be used maliciously.
9. Run the Spell tests by running `make test`. If there are concerns about potential modifications to the function, validators can bypass the `make` command and directly execute the test script using `./scripts/test-dssSpell-forge.sh`.
10. Wait for completion. Allow 20 to 60 minutes for the tests to complete.
11. Review and Save Results: Save the test results (pass or fail) for logging purposes.
