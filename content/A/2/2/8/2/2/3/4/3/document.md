---
id: 7f991abf-3395-4f92-82e1-88e991ebd97a
docNo: A.2.2.8.2.2.3.4.3
name: Required Primitive Inputs
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.4.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are defined herein and organized as two mutually exclusive pathways. Once the Review outcome is determined by the Facilitator, the corresponding Pathway is followed to the exclusion of the other.

- Operational Facilitator Approves Proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Approved`
            - `Commentary`
                - New value (optional): populate with reasoning for Approval
            - `Status`
                - New value: set to `Proposal Approved by Facilitator` [automated]
        - Responsible party: Operational Facilitator
        - Trigger-Process: [A.2.2.8.2.2.3.5 - Process Definition for Offchain Vote](24fa76f6-4728-4f1d-97ff-fd7e72dac2ac).
- Operational Facilitator Rejects Proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Rejected`
            - `Commentary`
                - New value (required): populate with reasoning for Rejection
            - `Status`
                - New value: set to `Proposal Rejected By Facilitator` [automated]
        - Responsible party: Operational Facilitator
