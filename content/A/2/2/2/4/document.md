---
id: dee40c3b-2f89-44c6-8813-c48888df08a7
docNo: A.2.2.2.4
name: Required Outputs
type: Core
depth: 5
childType: sections_and_primary_docs
---

###### A.2.2.2.4 - Required Outputs [Core]

This field specifies the particular Sky Core Atlas and/or Agent Artifact Documents that must be updated as an end result of a Process.

Where applicable, a Document Update can serve as a "trigger" that deterministically compels another Process Definition to be initiated by a system or actor. The `Trigger - Process` field links to the respective Process Definition that is triggered by the Required Output.

Some processes do not need formal "Required Outputs" because the only process flow step is a simple update of an Artifact Document. In these edge cases, the change specified in `Required Primitive Inputs` (e.g., toggling a field to Globally Activate a Primitive) fully completes the process, effectively completing it in a single step. Once the designated Document and field are updated as prescribed, the Process is considered finalized.
