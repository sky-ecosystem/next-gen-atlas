---
id: cd57f7e4-6acd-431e-97fd-89c3453c8eba
docNo: A.1.9.3.2.3
name: Debt Ceiling Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.3 - Debt Ceiling Breaker Exception [Core]

The LINE_MOM contract manages the breaker for the Debt Ceilings of a configurable subset of the vault types in the Sky Protocol. This Debt Ceiling Breaker allows a successful governance proposal to reduce the debt ceilings of a pre-configured whitelist of vault types to zero without waiting for the GSM Pause Delay to expire.

The Debt Ceiling Breaker affects both the Debt Ceiling and the Maximum Debt Ceiling of a given vault type when activated, disabling the Dynamic Debt Ceiling functionality for that vault type if enabled. To reverse the effect, parameters of affected vault types must be reconfigured with an Executive Vote which is subject to the GSM Pause Delay.

The whitelist may be configured via a successful governance proposal, but must wait for the GSM Pause Delay before changes come into effect. The whitelist is defined in [A.1.9.3.2.3.1 - Debt Ceiling Breaker Exception Whitelist](4937205a-5be0-4def-9b7f-00f9f3bff421) and can be changed via the Weekly Governance Cycle.
