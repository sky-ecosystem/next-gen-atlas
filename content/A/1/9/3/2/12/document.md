---
id: b9f3824c-31a5-472c-8a53-8166f3eeb7ee
docNo: A.1.9.3.2.12
name: stUSDS Bounded External Access Module Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.12 - stUSDS Bounded External Access Module Breaker Exception [Core]

The STUSDS_MOM contract allows Sky Governance to bypass the GSM Pause Delay and disable the stUSDS Bounded External Access Module or set the `cap` or `line` stUSDS parameters to zero.

This functionality allows Sky Governance to react more quickly in an emergency, e.g., if an operator of the stUSDS BEAM is hacked or is a malicious actor. Once the STUSDS_MOM is activated to disable the stUSDS BEAM, the stUSDS BEAM will not be able to change any stUSDS parameters in the system. If the STUSDS_MOM has been triggered, it will still be possible to modify stUSDS parameters through the usual Executive Vote process, subject to the GSM Pause Delay.
