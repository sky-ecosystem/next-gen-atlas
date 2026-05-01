---
id: 12bb55dc-8f44-4f7a-a7f8-bf197a278784
docNo: A.1.9.3.2.10.2
name: Stability Parameter Bounded External Access Module Exception
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.9.3.2.10.2 - Stability Parameter Bounded External Access Module Exception [Core]

The Stability Parameter Bounded External Access Module (SP-BEAM) MCD_SPBEAM contract manages the rates applied to Sky Protocol’s native vaults as well as the savings rates. Whitelisted operators can use the SP-BEAM to modify rates without waiting for the GSM Pause Delay. The SP-BEAM modifies rates up or down within specified parameters. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

This functionality allows the Sky Protocol to react to changes in market rates more quickly than waiting for an Executive Vote and the GSM Pause Delay.

The risk opened up by this functionality is malicious action by whitelisted operators setting rates to undesirable values. This risk can be mitigated through the SP-BEAM parameters and the SPBEAM_MOM.
