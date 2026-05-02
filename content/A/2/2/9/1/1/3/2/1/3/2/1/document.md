---
id: 1ac3e606-f1c7-4a20-a9b6-a425920e98d3
docNo: A.2.2.9.1.1.3.2.1.3.2.1
name: Core GovOps TRC Report Validation Process
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.3.2.1 - Core GovOps TRC Report Validation Process [Core]

Core GovOps receives TRC Reports from Primes on a regular basis and must perform the following validation process.

Core GovOps verifies against the Atlas any Ecosystem Accord referenced in the TRC Report for sourced Prime-External Junior Risk Capital (SEJRC) or rented Originated Senior Risk Capital (OSRC). This includes confirming the existence, current validity, and terms of such Accords as formally recorded within the Atlas.

Core GovOps validates the Prime Agent's reported IJRC by reconciling the reported IJRC amount and its constituent asset composition against the actual on-chain state of the Prime Agent’s designated SubProxy account. This involves direct on-chain verification of asset balances. Core GovOps verifies that all assets reported as IJRC and held within the SubProxy account meet the definition of "eligible assets" for IJRC as defined by the Atlas. See [A.3.2.1.2.2.1.1.1 - Internal Junior Risk Capital (IJRC)](8728abee-0dc5-449b-b4c2-78698da16f10).

For reported Tokenized External Junior Risk Capital (TEJRC) and Originated Senior Risk Capital directly originated by the Prime, Core GovOps validates the reported amounts and statuses by cross-referencing data from the relevant smart contract systems. This may involve querying TEJRC pool contracts, OSRC auction records, and other on-chain infrastructure to confirm the existence, ownership, and eligibility of these capital components.

Core GovOps reviews all attestations and disclosures made by the Prime Agent in the TRC Report. This review focuses on understanding the Prime Agent's TRC compliance with Aggregate RRC throughout the entire reporting period. This assessment is critical for identifying intra-period shortfalls that might not be visible to on-chain monitoring systems or reflected in the end-of-period snapshot alone. The assessment process may include requiring the Prime Agent to provide supplementary documentation, verifiable evidence, or independent third-party confirmations for material off-chain claims or attestations concerning intra-period events; and/or cross-referencing disclosed off-chain information with relevant on-chain indicators or transactions that might corroborate or contradict the attestations.

Finally, Core GovOps independently calculates and verifies the Prime Agent's compliance with all Atlas-defined capital sourcing ratios (e.g., External Per Internal (EPI), Senior Per Junior (SPJ)).
