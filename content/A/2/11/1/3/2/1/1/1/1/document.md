---
id: 3c0847fe-e117-40f8-86a3-9de56c9a3bba
docNo: A.2.11.1.3.2.1.1.1.1
name: Impact Assessment
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.11.1.3.2.1.1.1.1 - Impact Assessment [Core]

Impact Assessment defines the assessment process in which the potential impact of a Multisig compromise or failure is evaluated. The result of this evaluation is the assignment of an Impact Classification level as defined below. The Multisig Administrator is responsible for determining this classification and must provide it to Core GovOps as part of the Multisig registration process in accordance with [A.2.11.1.3.2.1.1.8 - Multisig Registration](110614e9-6375-464a-90b3-3b350d3cf79c).

| **Impact Classification Level** | **Financial Exposure** | **Decision Context** | **Reputational Impact** |
|---|---|---|---|
| Low | <$100k direct exposure | Minimal disruption, alternative paths exist | Limited scope impact |
| Medium | $100k – $1M exposure | Significant operational delays, workarounds available | Moderate reputational concern |
| High | $1M – $10M exposure | Major protocol disruption, difficult recovery | Serious reputational damage |
| Critical | >$10M exposure | Protocol-wide failure, catastrophic impact | Severe reputational damage |

When a Multisig falls between two classification levels, the higher security classification must be selected.
