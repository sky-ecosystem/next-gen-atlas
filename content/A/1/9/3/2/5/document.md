---
id: 2a0f27c9-7468-465d-9e07-19481f5e8c89
docNo: A.1.9.3.2.5
name: Direct Deposit Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.5 - Direct Deposit Breaker Exception [Core]

The DIRECT_MOM contract manages the breaker for Direct Deposit Modules (D3Ms). The breaker functionality allows a successful governance proposal to disable any or all of the active D3Ms. In practice, this will set the bar parameter to zero, which (contrary to intuition) disables the module by setting the allowed Debt Ceiling to zero. At this point, no further USDS can be minted through the Direct Deposit Module. To reverse the effect, parameters of affected Direct Deposit Modules must be reconfigured with an Executive Vote which is subject to GSM Pause Delay.

The risk opened up by this exceptional functionality is that a given line of USDS credit is unexpectedly shut down. This has the potential to disrupt the protocol in question, which may impact Sky indirectly.
