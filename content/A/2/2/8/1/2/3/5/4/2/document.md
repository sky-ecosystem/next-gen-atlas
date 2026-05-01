---
id: 1efa0fc5-5377-428f-a203-8c3c10dcc153
docNo: A.2.2.8.1.2.3.5.4.2
name: Agent Artifact Updates
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.3.5.4.2 - Agent Artifact Updates [Core]

The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.

- Proposal Passes
    - Required Primitive Input Trigger: Proposal Passes see [A.2.2.8.1.2.3.5.3 - Required Primitive Inputs](b593ff77-2c46-418d-a7b3-9730437ce804)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields
            - Invocation Status
                - New value: set to `Proposal Approved`
        - Responsible Party: Operational GovOps
        - Trigger - Process: [A.2.2.8.1.2.3.6 - Process Definition For Artifact Update](b3ed1e74-7ec2-4537-8e1d-2098dc17d984)
- Proposal Fails
    - Required Primitive Input Trigger: Proposal Fails see [A.2.2.8.1.2.3.5.3 - Required Primitive Inputs](b593ff77-2c46-418d-a7b3-9730437ce804)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields
            - Invocation Status
                - New value: set to `Proposal Rejected`
        - Other Document Operations:
            - `Instance Configuration Document` is `Archived` in Primitive Hub Document/Hub Data Repository
        - Responsible Party: Operational GovOps
