---
id: d034533f-9b6f-411c-8b60-3bccb374765f
docNo: A.2.2.9.1.1.3.2.1.2.2
name: Minimum Capabilities of Prime TRC Management Systems
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.2.2 - Minimum Capabilities of Prime TRC Management Systems [Core]

A Prime Agent’s internal TRC management system should possess the following capabilities to meet the objectives outlined in [A.2.2.9.1.1.3.2.1.2.1 - Objective of Prime TRC Management](9a8120c4-0a5b-426f-97a5-283c708413f5).

1. Prime Agents’ internal TRC management systems should enable compliant sourcing and tracking of all TRC components, including Internal Junior Risk Capital (IJRC), Prime-External Junior Risk Capital (SEJRC), Tokenized External Junior Risk Capital (TEJRC), and Originated Senior Risk Capital (OSRC). Compliance in this context includes strict adherence to eligibility criteria and capital-sourcing ratios (e.g., External Per Internal, Senior Per Junior) as defined in the Atlas. See [A.3.2.1.2.3 - Total Risk Capital Sourcing Ratios](9e99b084-f15a-4f60-b831-d6c0bd9aec04).
The system must provide real-time or near real-time tracking of all held Total Risk Capital (TRC) components. This includes, for each TRC component:
    - Accurate valuation of the assets comprising each component.
    - Clear identification of the source of each component (e.g., Prime’s own SubProxy for IJRC, specific Ecosystem Accord references for rented SEJRC or OSRC, TEJRC encumbrance details, OSRC origination details).
    - Verification of each TRC component’s eligibility status according to Atlas rules. This includes tracking whether capital is “enabled” or “active” for RRC coverage purposes (e.g., based on Ecosystem Accord status, compliance with sourcing ratios, etc.).
    - Distinction between capital directly held by the Prime Agent and capital that is encumbered (e.g., SEJRC where the lending Prime retains custody but the capital is contractually committed).
2. Prime Agents' internal TRC management systems should enable dynamic-state accounting. The system must account for TRC components that are in dynamic, pending, or off-chain states, as these can impact the true risk capital available to a Prime Agent. This includes:
    - Pending transactions such as SEJRC or OSRC rental Ecosystem Accords that have been committed to by the parties, but not yet codified in the Atlas.
    - Capital in transit, e.g., assets that are committed to be IJRC, but currently moving between chains via bridges or locked in Cross-Chain Transfer Protocol (CCTP) messages awaiting finality.
    - Operational expenditures funded by TRC components (typically IJRC), such as blockchain transaction fees, oracle service fees, audit costs, and other operational overhead that reduces available risk capital. The system should track these expenditures in real-time or near real-time.
    - Any off-chain factors that could impair the immediate deployability or availability of TRC components.
3. Prime Agents' internal TRC management systems should enable continuous capital adequacy monitoring. The system must enable the near real-time comparison of the Prime Agent's internally tracked and calculated TRC against its official Aggregate RRC, as obtained from the Sky Core RRC Dashboard. See [A.2.2.9.1.1.3.2.1.1 - Sky Core Required Risk Capital (RRC) Dashboard](4eac2c9e-2718-4881-a3f1-ed10fb3f4d13). This core functionality is essential for the Prime Agent to proactively monitor its capital adequacy, identify potential or actual TRC shortfalls, and make timely operational and capital management decisions to maintain compliance.
4. Prime Agents' internal TRC management systems should define a RRC-incident (e.g., TRC shortfall) response protocol. The system should enable internal alerting mechanisms that detect when a Prime Agent’s TRC approaches predefined internal buffer thresholds relative to its Aggregate RRC. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9). The system should also detect an actual shortfall where the Prime Agent’s held TRC falls below its Aggregate RRC. Furthermore, Prime Agent teams should establish and document internal processes for responding to such alerts. Such internal processes should include: 1) internal escalation and assessment of the shortfall’s cause and magnitude; 2) formulation of potential responses or corrective actions, which may include sourcing additional TRC, reducing risk-weighted exposures, or other measures; 3) internal decision-making framework for the evaluation of potential responses and selection of the most appropriate one; and 4) notifying any pertinent parties (Operational GovOps) as needed for the purpose of planning or implementing follow-up action.

Prime Agent teams' internal decision-making framework may consider the economic trade-offs of various actions, including the strategic acceptance of penalties for a TRC shortfall where such an approach is determined to be economically advantageous compared to immediate rebalancing (e.g., avoiding excessive transaction costs or market impact).
