---
id: d247fec5-a19d-4307-94de-a2cbcc368d64
docNo: A.2.2.8.2.2.3.5.3
name: Required Primitive Inputs
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.5.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are defined herein.

- After Facilitator prepares Snapshot vote:
    - Edit `Artifact Edit Proposal` Document
        - Updated fields
            - Status
                - New value: set to `Pending Poll`
            - Off-chain Snapshot
                - New value: Populate with link to the official Snapshot page
        - Responsible party: Operational Facilitator
- Mutually Exclusive Input Pathways: The two Primitive Inputs below are mutually exclusive pathways. Once the vote concludes, the corresponding Pathway is followed to the exclusion of the other.
    - Proposal Passes
        - Edit `Artifact Edit Proposal` Document
            - Update fields
                - Status
                    - New value: set to `Poll Approved`
            - Responsible party: Operational Facilitator.
            - Trigger - Required Output: Proposal passes
    - Proposal Fails
        - Updated fields
            - Edit `Artifact Edit Proposal` Document
                - Status
                    - New value: set to `Poll Rejected`
            - Responsible party: Operational Facilitator.
            - Trigger - Required Output: Proposal fails
