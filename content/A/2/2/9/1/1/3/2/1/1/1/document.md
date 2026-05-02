---
id: f7da0f56-00f5-4bcf-bd31-b77c284c7992
docNo: A.2.2.9.1.1.3.2.1.1.1
name: Role and Functionality of the RRC Dashboard
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.3.2.1.1.1 - Role and Functionality of the RRC Dashboard [Core]

The RRC Dashboard provides a user interface for Prime Agents to view their official RRC figures. The Dashboard provides the following key information:

- Instance Total RRC: For each specific Allocation System Primitive Instance, the system displays its Instance Total RRC. This figure is the sum of all applicable risk-specific RRC calculations for that Instance, including:
    - Instance Financial RRC ([A.3.2.1.1.4 - Instance Financial RRC](ba1d5c0e-399f-47a6-b5d4-b3f5477d5787))
    - Instance Smart Contract RRC ([A.3.2.1.1.5 - Instance Smart Contract RRC](4b4ea578-28b4-481c-9abd-d34c5a4f383c))
    - Instance Administrative RRC ([A.3.2.1.1.6 - Instance Administrative RRC](c2b60f0d-6555-463c-9ad3-2a9746be77c5))

The models for certain risk-factors are still currently under development. See [A.2.2.9.1.1.3.2.1.1.2 - Interim Notice Regarding RRC Dashboard Coverage](18243e7a-5b62-459d-83fb-e50b9df05f9d).

- Aggregate RRC: For each Prime Agent, the system displays its Aggregate RRC, which is the sum of all its Instance Total RRCs. This is the figure against which a Prime Agent’s Total Risk Capital (TRC) adequacy is assessed.
