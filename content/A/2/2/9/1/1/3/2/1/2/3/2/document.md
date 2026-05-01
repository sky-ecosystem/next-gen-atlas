---
id: 4887e971-be6c-4f98-9137-7cdec3ed0fa0
docNo: A.2.2.9.1.1.3.2.1.2.3.2
name: TRC Report Contents
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.2.3.2 - TRC Report Contents [Core]

The Total Risk Capital (TRC) Report submitted by a Prime Agent must provide an accurate and verifiable breakdown of all TRC components held by the Prime Agent as of the end of the specified reporting period. The TRC Report should include the following essential information:

- Aggregate TRC Value As of End of Period: The total declared value in USD of all eligible TRC components held by the Prime Agent as of the end of the reporting period.
- Detailed Breakdown of TRC Components As of End of Period: For each category of TRC held, the report must detail the following values as of the end of the reporting period:
    - Internal Junior Risk Capital (IJRC): The total amount of IJRC, a breakdown of its constituent asset types, and their respective values in USD.
    - Prime-External Junior Risk Capital (SEJRC): The total amount of SEJRC. For each portion of SEJRC sourced from another Prime Agent, the report must include the amount in USD, the identifier of the counterparty Prime Agent, the expiry date of the arrangement, and a direct reference to the Ecosystem Accord that governs the SEJRC arrangement.
    - Tokenized External Junior Risk Capital (TEJRC): The total amount of TEJRC. For each TEJRC source, the report must include the amount in USD, the identifier of the TEJRC smart contract or facility and any relevant encumbrance identifier.
    - Originated Senior Risk Capital (OSRC): The total amount of OSRC. The report must specify the amount originated directly by the Prime Agent from the Total Senior Risk Capital (TSRC) pool and any amount of OSRC rented from other Prime Agents. For any rented OSRC, the report must include the amount in USD, the identifier of the counterparty Prime Agent, the expiry date, and a direct reference to the pertinent Ecosystem Accord.
    - Key Ratio Inputs and Computed Totals (Prime Internal Calculation) As Of End Of Period: Based on the component values reported above (as of the end of the reporting period), the report must include key figures used in and resulting from the Prime Agent's internal capital adequacy calculations. These figures reflect the capital structure and ratios as of the end of the reporting period and include:
        - Internal Junior Risk Capital (IJRC)
        - External Junior Risk Capital (EJRC) generated via External Per Internal Ratio (Prime External Junior Risk Capital + Tokenized External Junior Risk Capital sourced via the EPI ratio still carries Senior Per Junior or SPJ capacity)
        - EJRC-via-SPJ (sourced by spending SPJ capacity; zero-SPJ-capacity thereafter)
        - Enabled Senior Risk Capital (SRC)
        - Total Senior Per Junior capacity
            - Allocation of SPJ capacity to 1) enable SRC; or to 2) source EJRC
        - Prime-computed eligible Total Risk Capital (IJRC + EJRC-via-EPI + EJRC-via-SPJ + enabled SRC)
        - Official Aggregate RRC
        - Capital buffer = TRC – Aggregate RRC
        - Effective ratios
            - EPI = EJRC-via-EPI ÷ IJRC
            - SPJ utilisation:
                - enabled SRC ÷ total SPJ capacity
                - EJRC-via-SPJ ÷ total SPJ capacity
- Dynamic Period Attestation and Disclosures: In addition to the end-of-period snapshot figures, the TRC Report must include an Attestation from the Prime Agent confirming it maintained TRC at or above its Aggregate RRC at all times throughout the entire reporting period. In addition, the TRC Report must include disclosure of any events, Prime-initiated off-chain contractual obligations, impairments to the value or redeemability of held assets (such as RWA backing or bridged asset viability), encumbrances, or other conditions that occurred at any point during the reporting period which materially affected its TRC, even if such conditions were temporary or not continuously visible to on-chain monitoring systems. This disclosure must include the nature of the event/condition, its precise timing and duration, and its quantified impact on the Prime Agent's TRC.
