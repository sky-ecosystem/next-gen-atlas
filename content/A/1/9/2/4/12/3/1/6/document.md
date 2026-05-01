---
id: 0ad70737-d32f-4c50-a4ff-d3f505e171c2
docNo: A.1.9.2.4.12.3.1.6
name: Spell Validators Must Check Deployed Spell Was Not Deployed Using CREATE2
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.6 - Spell Validators Must Check Deployed Spell Was Not Deployed Using CREATE2 [Core]

Validators must ensure that no contract, neither the Spell Executive contract (DssSpell / DssExec) nor the Spell Action contract (DssSpellAction / DssAction) - was deployed using the `CREATE2` opcode.

To perform this validation, the validator must:

- Locate and copy the contract creation transaction on Etherscan. The contract creation transaction can be found under the "internal transactions" tab on Etherscan.
- Use a transaction decoder, such as Tenderly or another blockchain analysis tool, to decode the transaction hash and identify the opcode used during deployment.
- Ensure the opcode is `CREATE`. If `CREATE2` is used, the Spell fails validation.
