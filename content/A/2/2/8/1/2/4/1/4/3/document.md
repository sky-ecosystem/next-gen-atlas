---
id: 6b90e3a1-48ce-4ac2-852e-00a8e4edf152
docNo: A.2.2.8.1.2.4.1.4.3
name: Required Primitive Inputs
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.8.1.2.4.1.4.3 - Required Primitive Inputs [Core]

The required Primitive Inputs to this process are specified herein and organized as sequential stages.

- Core GovOps adds reimbursement to Executive Vote
    - Edit `Sky Core Distribution Reward Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement/Executive Vote
                - New value: links to proposal
            - Status
                - New value: set to `Added to Executive Vote`
- After Executive Vote passes, Core GovOps updates Powerhouse system
    - Edit `Sky Core Distribution Reward Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement / Transaction Details/ Amount Paid
                - New value: populate with amount paid to reimburse Operational Executor Agent Buffer
            - Executive Vote Settlement / Transaction Details / Tx Hash
                - New value: Populate with transaction hash
            - Status
                - New value: set to `Completed`
