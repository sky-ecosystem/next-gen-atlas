---
id: 49997c91-ec3c-47be-ad1a-abfd33dd259b
docNo: A.1.9.5.3.1.3.6
name: Determining Protego Parameters
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.5.3.1.3.6 - Determining Protego Parameters [Core]

The parameters for the scheduled Spell to be canceled, as specified in [A.1.9.5.3.1.3 - Protego Parameters](55195cdc-90c3-4133-a0e4-792444b60ed8), should always be determined by inspecting the logs emitted from the `plot` function of the Pause contract. The parameters should never be determined by calling functions on the Spell to be canceled, because these functions may not return the correct values in the case of a malicious Spell.
