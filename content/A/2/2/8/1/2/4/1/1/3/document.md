---
id: 57921647-2a63-4d01-907b-131a50510d76
docNo: A.2.2.8.1.2.4.1.1.3
name: Required Primitive Inputs
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.4.1.1.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are specified herein.

- Edit `Distribution Reward Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `In Progress`
        - Underlying data
            - New value: populate with underlying data used to calculate the eligible USDS and sUSDS balances
        - Eligible USDS balance
            - New value: populate with calculated value
        - Eligible sUSDS balance
            - New value: populate with calculated value
        - Distribution Reward Due
            - New value: populate with calculated value.
    - Responsible party: Operational GovOps.
    - Trigger-Process: [A.2.2.8.1.2.4.1.2 - Process Definition For Reward Issuance From Operational Executor Agent Buffer](ddd65b02-3a2b-4478-a435-989324c2f1b8).
