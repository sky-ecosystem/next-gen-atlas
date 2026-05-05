---
id: e9422783-6196-4117-9099-b5ec0c338c05
docNo: A.2.2.2.3.1
name: Sequential Stages
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.2.2.2.3.1 - Sequential Stages [Core]

Some Processes require Primitive Inputs that are organized into multiple sequential stages (also called "Input stages"). Each Input stage must be completed before progressing to the next, ensuring that all dependencies and validations are met in order. Once an Input stage is completed, the subsequent Input stage is initiated automatically, continuing in this manner until all stages have been finished.

Upon completing the final Primitive Input stage, the Process Definition transitions to the `Required Outputs` schema component; this component defines the necessary updates to Sky Core Atlas or Agent Artifact Documents.
