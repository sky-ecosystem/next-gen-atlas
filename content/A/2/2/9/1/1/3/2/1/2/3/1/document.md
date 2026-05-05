---
id: 7e95efa7-e409-48dc-9b5a-96edce54bf31
docNo: A.2.2.9.1.1.3.2.1.2.3.1
name: Mandate and Rationale
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.2.3.1 - Mandate and Rationale [Core]

Prime Agents are required to periodically submit TRC Reports to Core GovOps. This report serves a dual purpose. It provides a verifiable snapshot of the Prime Agent's TRC composition and key capital ratios as of the end of the reporting period; and second, it provides a formal attestation regarding the Prime Agent's maintenance of TRC at or above its dynamically changing Aggregate Required Risk Capital (RRC) throughout the entire reporting period. See [A.3.2.1.1.2 - Aggregate RRC](6aed5cc1-9671-4b73-88a9-fdd86ac93ece).

This comprehensive reporting, encompassing both an end-of-period statement and disclosures of any intra-period events affecting TRC, is essential. On-chain data alone (such as that captured by the planned OVRC system) cannot definitively prove the full eligibility and unimpaired availability of a Prime Agent's capital position for continuous RRC coverage, nor can it capture all off-chain factors. These factors include, but are not limited to, whether assets are subject to Prime-initiated off-chain contractual pledges, if the economic value or redeemability of its bridged assets is compromised by issues with their originating bridge, or if its assets are encumbered by derivative structures or other off-chain commitments that would impair their immediate use at any point during the period.

The TRC Report serves as an important basis for Core GovOps’ verification procedures. This entails: 1) reconciling reported end-of-period TRC components against the Sky Atlas, on-chain data, and other relevant sources to validate the period-end capital position and adherence to Atlas-defined capital requirements; and 2) reviewing Prime Agents’ attestations and disclosures regarding its TRC management and any material events throughout the reporting period to assess continuous compliance with its dynamically changing Aggregate RRC. The outcome of this validation is a critical input for the monthly settlement cycles, which latter includes the determination and retroactive application of penalties for any identified discrepancies or violations of capital requirements during the period.

The long-term vision is for the Powerhouse system to enable the automation of TRC data aggregation and verification. The Powerhouse system will have capabilities such as directly querying Prime Agent SubProxy accounts for IJRC assets, programmatically accessing and interpreting Ecosystem Accords recorded in the Atlas, interfacing with TEJRC and OSRC smart contract systems, and automatically applying Atlas-defined eligibility rules. See [A.2.2.9.1.1.3.2.1.3.1 - Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC)](8048bdf0-84b7-4546-8f1a-98b62d073c84). Even in this advanced state, the TRC Report, or a similar form of periodic attestation, may remain necessary to cover elements of TRC verification that are not fully able to be automated or require explicit Prime Agent declaration.
