---
id: 11161730-6568-445f-a250-ba5c67857390
docNo: A.2.2.8.1.2.3.1.4.2
name: Agent Artifact Updates
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.3.1.4.2 - Agent Artifact Updates [Core]

The Agent Artifact is updated pursuant to the following requirements. Each Output "set" is triggered following the completion of its respective Input stage, defined in [A.2.2.8.1.2.3.1.3 - Required Primitive Inputs](4d5482ad-7944-4073-8fbe-b9dbcd1a27a3).

- After Prime Agent's `Initial planning document` Status is set to `Drafting`
    - Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository.`
        - Instance Status: (automatically inherits from `Primitive Hub Document`)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Planning`
            - Instance Configuration Document Location
                - New value: link to `Instance Configuration Document` (created at Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository.`)
    - Responsible party: Operational GovOps [automated]
- After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
    - Edit `Primitive Hub Document/In Progress Invocations/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Pending GovOps review`
        - Responsible party: Operational GovOps [automated]
        - Trigger - Process: [A.2.2.8.1.2.3.2 - Process Definition For Operational GovOps Review](5fd265ef-17f0-4400-b06c-a6ce9fa87636).
