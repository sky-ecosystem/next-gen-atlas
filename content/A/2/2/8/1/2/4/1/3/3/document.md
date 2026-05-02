---
id: b55afaef-db92-4bbf-8d80-258d5849ef1c
docNo: A.2.2.8.1.2.4.1.3.3
name: Required Primitive Inputs
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.4.1.3.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are specified herein and are mutually exclusive pathways.

- Core GovOps Confirms Accuracy of Payment
    - Edit `Distribution Reward Payments` Active Data Document
        - Updated fields
            - Core GovOps Review/Confirmation
                - New value: populate with Yes
            - Core GovOps Review/Commentary
                - New value (optional): populate with reasoning
        - Responsible party: Core GovOps
        - Trigger - Process: [A.2.2.8.1.2.4.1.3.4.1 - Sky Core Atlas Updates](cca17fe9-3dc9-48ce-be26-39a1625b3690)
- Core GovOps Finds Inaccurate Payment
    - Edit `Distribution Reward Payments` Active Data Document
        - Updated fields
            - Core GovOps Review/Confirmation
                - New value: populate with No
            - Core GovOps Review/Commentary
                - New value (required): populate with reasoning
        - Responsible party: Core GovOps
        - Trigger - Process: Payment Inaccuracy Previously Found By Core GovOps
