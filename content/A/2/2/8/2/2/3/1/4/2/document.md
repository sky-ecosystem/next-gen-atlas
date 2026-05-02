---
id: d86e5f9f-7b1c-4605-9253-4281a6bdbc13
docNo: A.2.2.8.2.2.3.1.4.2
name: Agent Artifact Updates
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.1.4.2 - Agent Artifact Updates [Core]

The Agent Artifact is updated pursuant to the following requirements. Each Output "set" is triggered following the completion of its respective Input stage, which latter is defined in [A.2.2.8.2.2.3.1.3 - Required Primitive Inputs](b91d0eb6-fa86-486c-8350-4564bdb5af09).

- After Prime Agent's `Initial planning document` Status is set to `Drafting`
    - Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository`.
        - Instance Status: (automatically inherits from `Primitive Hub Document`)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Planning`
            - Instance Configuration Document Location
                - New value: link to `Instance Configuration Document` (created at Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository`.)
    - Responsible party: Operational GovOps [automated]
- After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
    - Edit `Primitive Hub Document/In Progress Invocations/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Pending GovOps review`
        - Responsible party: Operational GovOps [ automated]
        - Trigger - Process: [A.2.2.8.2.2.3.2 - Process Definition for Operational GovOps Review](38c54d2b-715b-433d-a9ff-af5cbecc89a2).
