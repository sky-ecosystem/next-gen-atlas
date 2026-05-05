---
id: 4d5482ad-7944-4073-8fbe-b9dbcd1a27a3
docNo: A.2.2.8.1.2.3.1.3
name: Required Primitive Inputs
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.3.1.3 - Required Primitive Inputs [Core]

The required Primitive Inputs for this process are defined herein and organized in sequential stages.

- Drafting of Initial Planning Document
    - Create `Initial Planning Document`
        - Updated fields
            - `Status`
                - New value: set to `Drafting`
            - `Integrator`
                - New Value: set to Integrator Name
            - `Reward Code`
                - New Value: set to Reward Code
            - `Tracking Methodology`
                - New value: populate with details for tracking utilization
            - `Custom Instance Parameters`
                - New Value: populate with details for any custom parameters
        - Responsible Party: Prime Agent Team
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Drafting`
- Initial Planning Document Triggered For GovOps review
    - Edit `Initial Planning Document`
        - Updated fields
            - `Tracking Methodology`
                - New value: updated content, as applicable
            - `Status`
                - New value: set to `Ready for GovOps Review`
        - Responsible party: Prime Agent
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
