---
id: 103a2e8f-fcc4-4044-ba46-21f7e8351bac
docNo: A.1.10.3.2.10.4
name: Smart Burn Engine Bounded External Access Module Exception
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.10.3.2.10.4 - Smart Burn Engine Bounded External Access Module Exception [Core]

The Smart Burn Engine Bounded External Access Module (SBE-BEAM) manages certain parameters of the Smart Burn Engine. See [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a). Whitelisted operators can use the SBE-BEAM to modify the `kbump`, `burn`, and `hop` parameters without waiting for the GSM Pause Delay. The SBE-BEAM modifies these parameters, up or down, within specified bounds. See [A.3.5.2.4 - Smart Burn Engine Bounded External Access Module](b57ac61b-f6b1-4025-bd44-569d0f2afe2f).

This functionality allows the Sky Protocol to update Smart Burn Engine parameters more quickly than waiting for an Executive Vote and the GSM Pause Delay.

The risk opened up by this functionality is malicious action by whitelisted operators setting Smart Burn Engine parameters to undesirable values. This risk can be mitigated through the SBE-BEAM parameters and the SPLITTER_MOM, as specified in [A.1.10.3.2.8 - Smart Burn Engine Breaker Exception](5247c795-7f9d-4d3f-a040-6bc9b070e2d4).
