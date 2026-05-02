---
id: adfb66a3-4f73-4fcc-bfa2-f5126503187c
docNo: A.2.2.8.2.2.3.5.4.2
name: Agent Artifact Updates
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.2.2.3.5.4.2 - Agent Artifact Updates [Core]

The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.
The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.

- Proposal passes
    - Required Primitive Input Trigger: Proposal Passes
    - **Edit** `Primitive Hub Document`
        - Fields Updated
            - Active instances/instance name/instance status - set to `Approved`
        - Responsible Party: Operational GovOps
        - Trigger - Process: [A.2.2.8.2.2.3.6 - Process Definition for Artifact Update](182ca3dc-108f-4941-ae2e-eb01c345125b).
- Proposal fails
    - Required Primitive Input Trigger: Proposal Fails
    - **Edit** `Primitive Hub Document`
        - Fields Updated
            - Active instances/instance name/instance status - set to `Rejected`
        - Other Document Operations:
            - `Instance Configuration Document` is `Archived` in Primitive Hub Document/Data Repository
        - Responsible Party: Operational GovOps
