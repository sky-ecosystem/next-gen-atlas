---
id: a6940e22-f25c-4f29-9307-328b7f590ce7
docNo: A.1.9.2.4.12.3.3.7
name: Spell Validators Should Review Constants
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.7 - Spell Validators Should Review Constants [Core]

Validators should ensure that the rates are defined as per-second accumulation values, using the correct precision units common in the Sky Protocol (e.g., RAY for rates, RAD for debt/DAI amounts, WAD for general token amounts).

**Precision Units Overview**:

- **WAD (10^18)**: Used for token amounts and balances.
- **RAD (10^45)**: Used for debt values, ceilings, or large accumulations.
- **RAY (10^27)**: Used for rates and multipliers.

These units prevent floating-point issues in Solidity — always confirm they're applied correctly to avoid overflows or miscalculations. Group this with general constant validations (e.g., ensuring hardcoded values like fees or ceilings are computed accurately).

Rate values can be validated against the commented rate by using the `bc` command in a bash shell. Using the `NEW_FEE` variable in the example contract the following is visible: `bc -l <<< 'scale=27; e( l(1.095)/(60 * 60 * 24 * 365) )`. This produces 1.000000002877801985002875644. Removing the decimal place will allow you to see that this matches the definition of `NEW_FEE`.

Validating all rate adjustments can be done the same way. For more information on the rates module, refer to the developer guide ([https://github.com/sky-ecosystem/developerguides/blob/master/mcd/intro-rate-mechanism/intro-rate-mechanism.md](https://github.com/sky-ecosystem/developerguides/blob/master/mcd/intro-rate-mechanism/intro-rate-mechanism.md)). For easy reference, common pre-computed rates can also be viewed at the following ipfs link ([https://ipfs.io/ipfs/QmefQMseb3AiTapiAKKexdKHig8wroKuZbmLtPLv4u2YwW](https://ipfs.io/ipfs/QmefQMseb3AiTapiAKKexdKHig8wroKuZbmLtPLv4u2YwW)).

Immediately prior to making rate changes, `drip` must be called on the respective contracts.
