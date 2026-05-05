---
id: 10c53693-4784-40ad-a8c6-fd2551f14280
docNo: A.2.2.2.4.1
name: Multiple Required Outputs And Their Respective Input Stage or Mutually Exclusive Pathway
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.2.2.2.4.1 - Multiple Required Outputs And Their Respective Input Stage or Mutually Exclusive Pathway [Core]

Where a Process Definition has more than one set of Required Outputs, and each set corresponds to (or is "triggered by") either a specific Input stage or a specific Mutually Exclusive Input Pathway, the Process Definition’s `Required Primitive Input` field must define which `Required Output` set is Invoked upon completion of that stage or pathway.

1. **For Sequential Stages**: When multiple sequential stages exist, each stage’s successful completion triggers its corresponding Required Output set. As subsequent stages are completed in turn, each triggers its own distinct Required Outputs, ensuring that all designated outputs eventually execute in sequence.
2. **For Mutually Exclusive Pathways**: If the Required Primitive Input process instead (or additionally) involves mutually exclusive paths, once a pathway is chosen—either manually or automatically by a specified condition—only the Required Output set tied to that pathway is applied. Outputs associated with the unselected/unexecuted pathways remain inactive.
