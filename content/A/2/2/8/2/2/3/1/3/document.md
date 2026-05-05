---
id: b91d0eb6-fa86-486c-8350-4564bdb5af09
docNo: A.2.2.8.2.2.3.1.3
name: Required Primitive Inputs
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.1.3 - Required Primitive Inputs [Core]

The required Primitive Inputs for this process are defined herein and organized in sequential stages.

- Drafting of Initial Planning Document
    - Create `Initial Planning Document`
        - Updated fields
            - `Status`
                - New value: set to `Drafting`
            - `Integration Partner Name`
                - New Value: set to Integration Partner name
            - `Integration Partner Reward Address`
                - New Value: set to Integration Partner reward address
            - `Integration Partner Chain`
                - New Value: set to Integration Partner chain
            - `Integration Boost Cadence`
                - New Value: set to Integration Boost cadence
            - `Integration Boost Data Submission Format`
                - New Value: populate with details for format of data submission
            - `Integration Boost Data Submission Responsible Actor`
                - New Value: set to Actor responsible for data submission
            - `Integration Boost Savings Rate Adjustment Strategy`
                - New Value: populate with details for handling adjustments to Sky Savings Rate
            - `Custom Instance Parameters`
                - New Value: populate with details for any custom parameters
        - Responsible Party: Prime Agent Team
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Drafting`
- Initial Planning Document triggered for GovOps review
    - Edit `Initial Planning Document`
        - Updated fields
            - `Integration Boost Savings Rate Adjustment Strategy`
                - New value: updated content, as applicable
            - `Status`
                - New value: set to `Ready for GovOps Review`
        - Responsible party: Prime Agent
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
