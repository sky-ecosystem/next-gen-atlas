---
id: de343461-5583-4157-b71a-a15e3e3b1ad1
docNo: A.1.9.2.4.12.3.3.10
name: Spell Validators Should Review Contract For Unusual Elements
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.10 - Spell Validators Should Review Contract For Unusual Elements [Core]

Validators should assess whether any unusual or unexpected elements appear in the contract. It could be:

- Hidden state changes: Look for retrieval functions (e.g., `get` or `view`) that include assignments (`=`), indicating state changes.
- External Calls At The End: Check for external calls (e.g., `.call`, `.send`, `.transfer`) made after state changes, as this could indicate potential reentrancy attacks.
- Force Ether, DAI or SKY Reception: Look for a `receive` function with no logic, which could forcibly receive assets.
- Use of `tx.origin`: The tx.origin variable refers to the address that started the current transaction. If `tx.origin` is used instead of `msg.sender` in decision-making processes, it could lead to unintended authorization.
- Function Naming Overlaps: A contract might have function names that are similar or overlap with common Solidity functions to mislead a reviewer. Check for misleading function names (e.g., `transfer`, `approve`, `mint`) with unexpected logic or assignments.

To perform this validation the validator must go to the "Contract" tab on Etherscan and review the source code.
