---
id: 5ce20b57-b8bb-4a67-b5b6-a28b707e2cb2
docNo: A.1.9.3.2.10.3
name: stUSDS Bounded External Access Module Exception
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.9.3.2.10.3 - stUSDS Bounded External Access Module Exception [Core]

The stUSDS Bounded External Access Module (stUSDS BEAM) manages the parameters of the stUSDS system. Whitelisted operators can use the stUSDS BEAM to modify certain stUSDS parameters without waiting for the GSM Pause Delay. The stUSDS BEAM modifies stUSDS parameters within specified ranges. See [A.4.4.1.3.8 - stUSDS Bounded External Access Module](37f8f82e-7239-4cfb-8f95-d2cc40515cd9).

This functionality allows the Sky Protocol to update stUSDS parameters more quickly than waiting for an Executive Vote and the GSM Pause Delay.

The risk opened up by this functionality is malicious action by whitelisted operators setting stUSDS parameters to undesirable values. This risk can be mitigated through the stUSDS BEAM parameters and the STUSDS_MOM.
