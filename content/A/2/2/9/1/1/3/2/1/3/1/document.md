---
id: 8048bdf0-84b7-4546-8f1a-98b62d073c84
docNo: A.2.2.9.1.1.3.2.1.3.1
name: Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC)
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.3.1 - Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC) [Core]

An autonomous monitoring system must be designed and implemented to enable continuous tracking of Prime Agents’ on-chain verifiable risk-capital components in near real-time. The on-chain, verifiable risk-capital components that can be tracked by such a monitoring system in real time are termed "On-chain Verifiable Risk Capital" (OVRC).

OVRC is not necessarily equivalent to Total Risk Capital (TRC). A Prime Agent’s actual TRC cannot be determined definitively without accounting for off-chain agreements, encumbrances or other relevant conditions affecting capital eligibility or availability, which conditions must be disclosed in the TRC Reports submitted by Prime Agents. See [A.2.2.9.1.1.3.2.1.2.3 - Primes’ TRC Report](41ca2085-d71b-47e5-8b1a-b183b6e2b6fc).

Where the OVRC of a Prime Agent is less than its Aggregate RRC, the shortfall will be logged and penalty accrual will commence on a pro-rata, per-second basis for the duration and magnitude of the observed shortfall, according to the penalty schedule defined in the Atlas. Thus, this on-chain monitoring system serves as an interim penalty ledger.
