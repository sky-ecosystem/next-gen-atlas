---
id: 01214a59-5119-4c77-ad41-c9d3dd72a517
docNo: A.2.2.8.2.2.3.3.3
name: Required Primitive Inputs
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.3.3 - Required Primitive Inputs [Core]

The required Primitive Inputs for this process are defined herein and implemented in sequential stages.

- Agent creates `Artifact Edit Draft` document; drafting in progress
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `In Progress`
            - Content
                - New value: populate with drafted content
- Agent finalizes `Artifact Edit Draft`
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `Draft Finalized`
- Powerhouse System Creates `Artifact Edit Proposal` Document
    - Updated fields
        - Content
            - New value: Inherits data from `Artifact Edit Draft` Document’s Content field.
    - Responsible party: Operational GovOps [if not automated]
- Agent submits `Artifact Edit Proposal` Document to Powerhouse system
    - Updated fields
        - Status:
            - New value: set to `Pending Facilitator Review`
    - Responsible Party: Agent
