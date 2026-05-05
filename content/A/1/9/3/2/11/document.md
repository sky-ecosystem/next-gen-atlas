---
id: 1fd7d164-e9f3-4d6c-ab5e-0122bb415f8d
docNo: A.1.9.3.2.11
name: Stability Parameter Bounded External Access Module Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.11 - Stability Parameter Bounded External Access Module Breaker Exception [Core]

The SPBEAM_MOM contract allows Sky Governance to bypass the GSM Pause Delay and disable the Stability Parameter Bounded External Access Module.

This functionality allows Sky Governance to react more quickly in an emergency, e.g., if an operator of the SP-BEAM is hacked or is a malicious actor. Once the SPBEAM_MOM is activated, the SP-BEAM will not be able to change any rates in the system. If the SPBEAM_MOM has been triggered, it will still be possible to modify rates through the usual Executive Vote process, subject to the GSM Pause Delay.
