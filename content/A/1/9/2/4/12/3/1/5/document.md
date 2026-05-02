---
id: 354e4b28-61fd-4416-aa8b-085e40cdf920
docNo: A.1.9.2.4.12.3.1.5
name: Spell Validators Must Check Deployed Spell Is Not A DarkSpell
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.1.5 - Spell Validators Must Check Deployed Spell Is Not A DarkSpell [Core]

Validators must confirm that the deployed Spell does not execute an external `DssAction` contract. This validation ensures that the Spell is self-contained, does not rely on external contracts or pre-defined Ethereum addresses, and that the `DssExec` and `DssSpellAction` contracts are deployed together and not separately, as is done when using DarkSpells. Validators must perform the following two checks:

1. Check that the DssAction contract’s `execute()` function only calls the `actions()` function and does not interact with any external contracts or explicitly defined Ethereum addresses.
2. Check that the second argument used in the constructor when instantiating the `DssExec` is a newly created Spell action contract (e.g. `address(new DssSpellAction())`) and not an explicitly defined Ethereum address. This confirms that the Spell is linked to the correct action contract.

If either of these checks fails, the Spell cannot pass validation.

The validation checks can be performed by navigating to the "Contract tab" on Etherscan for the deployed Spell. In the source code, first locate the `DssAction` contract (or its equivalent, such as `DssSpellAction`). Review the `execute()` function and make sure that it only calls the `actions()` function. Then, locate the constructor and confirm that the `action` argument is instantiated as a new contract.
