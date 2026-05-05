---
id: 4c84f0a6-0d4d-4718-a7c4-04fa29fadfcc
docNo: A.2.2.8.2.2.4.1.1.3
name: Required Primitive Inputs
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.4.1.1.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are specified herein.

- Edit `Integration Boost Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `In Progress`
        - Underlying data
            - New value: populate with underlying data used to calculate the net deposits
        - Net deposits
            - New value: populate with calculated value
        - Integration Boost payment due
            - New value: populate with calculated value.
    - Responsible party: Operational GovOps.
    - Trigger-Process: [A.2.2.8.2.2.4.1.2 - Process Definition For Integration Boost Payment Issuance From Operational Executor Agent Buffer](16474cb5-8af4-4f11-b0c1-2c00f292cc2b).
