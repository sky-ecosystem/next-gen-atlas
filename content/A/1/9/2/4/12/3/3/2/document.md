---
id: b28afb60-f8cc-4529-9775-1a3a0e22efed
docNo: A.1.9.2.4.12.3.3.2
name: Spell Validators Should Review Spell Constructor
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.2 - Spell Validators Should Review Spell Constructor [Core]

Validators should ensure that the Spell constructor is properly implemented. The constructor is a critical part of the Spell contract, as it defines key parameters such as the Spell's expiry time and the inclusion of the `DssSpellAction` code block, which specifies the actions the Spell will execute.

Validators should follow these steps to review the constructor:

- Navigate to the "Contract" tab on Etherscan and scroll to the bottom of the contract source code to locate the constructor declaration.
    - Verify that the Spell inherits from the `DssExec` contract, which serves as the base contract for all Sky Spells.
    - Verify that the constructor is properly implemented with the correct parameters. For example, the expiry time should be set to the correct duration (e.g., `30 days`).
