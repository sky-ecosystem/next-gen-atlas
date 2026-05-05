---
id: 8ee36ed9-cae6-462b-a6b4-9aa5479fee18
docNo: A.1.9.2.4.13.4.2
name: Execution Of Spell
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.13.4.2 - Execution Of Spell [Core]

Within the same transaction initiated by `cast()`, ds-pause proceeds as follows:

1. Validation and Removal: The `exec` function in `ds-pause` validates the execution request and removes it from the list of scheduled executions.
2. Delegate Call to Spell Action Contract: The `ds-pause` contract calls `exec` on the Pause Proxy contract, which performs a `delegatecall` to the Spell action contract address specified during scheduling.
3. Execution of Spell Actions:
    - For regular Spells, the Pause Proxy calls the `execute()` function on the `DssSpellAction` contract.
    - The `execute()` function calls the `actions()` function, where the Spell’s actions are carried out.
4. Error Handling: If the transaction reverts at any point (e.g., due to an error in `actions()`), the Pause Proxy halts execution.
5. Final Checks: If the transaction succeeds, the `exec` function in `ds-pause` performs a final ownership check to ensure the Pause Proxy is still owned by `ds-pause`.
6. Completion: Once the final check passes, the execution of `cast()` is finalized, marking the end of the process.
