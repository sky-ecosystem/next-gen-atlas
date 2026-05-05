---
id: e15ea323-038d-4935-a39e-295c152251da
docNo: A.1.9.2.3.2.3.1.1.2.7.1
name: Validation Checks By StarGuard
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.1.9.2.3.2.3.1.1.2.7.1 - Validation Checks By StarGuard [Core]

The following checks are enabled by the contract:

- Verifies that the whitelisted Spell is executable only once, enforcing single-use to prevent replay attacks or unauthorized repeats.
- Verifies that the whitelisted bytecode codehash is valid, protecting against tampering or malicious alterations.
- Verifies that the Spell meets custom requirements (e.g., office hours) by confirming the `spell.isExecutable()` view function returns true.
- Verifies that StarGuard retains access to the SubProxy, ensuring no loss of control during the Agent Spell execution.
