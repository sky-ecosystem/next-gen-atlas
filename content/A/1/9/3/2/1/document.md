---
id: 3041b5f2-36f4-49c5-b1ca-f0c97d6e63b2
docNo: A.1.9.3.2.1
name: Executive Drop Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.1 - Executive Drop Exception [Core]

The MCD_PAUSE contract manages the general governance timelock of the GSM Pause Delay; however, it also contains an in-built exception to its own rule.

The executive drop functionality allows a successful governance proposal to cancel a previous governance proposal that has not yet passed the GSM Pause Delay period and been executed. As in any other situation, the new Executive proposal must be the hat proposal, meaning more SKY is voting for it than is voting for any other Executive proposal.

This functionality allows Sky Governance to prevent a malicious attack on the protocol if they are able to exceed the attacker’s SKY weight before the GSM Pause Delay expires.

The risk opened up by this exceptional functionality is that a malicious attacker may be able to delay or permanently block a legitimate governance proposal.
