---
id: 095edfd9-1a87-46f1-a5a5-7ff8f3d26eb1
docNo: A.1.2.2.2.15
name: The Active Data Controller Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.15 - The Active Data Controller Type [Type Specification]

[See below]

**Components**:

"Content": The Content Component of Active Data Controller Documents is used to define: 1) the entities who are authorized to modify the child Active Data Documents and 2) the authorized process by which said Active Data Documents are modified. If applicable, the Custom Components format and requirements of the Active Data Documents must be defined as well.

**Doc Identifier Rules**:

Active Data Controller Documents follow the Document Identifier Rules of Primary Documents. Active Data Controller Documents have Document Identifiers that are 4 layers or deeper in the Document Tree, and cannot contain 0's [zeros]. Within these constraints, Active Data Controller Documents can have whatever Document Identifier that is useful for their purpose.

**Additional Logic**:

Active Data Controller Documents must have an Active Data Directory Document located below it at the .0.6 position. The Active Data Controller Document can reference its Active Data subdocuments for its own logic. This allows Active Data Documents to be self-improving and adaptive at high speeds.

**Type Category**:

Primary Document

**Type Name**:

Active Data Controller

**Type Overview**:

Active Data Controller Documents are Primary Documents that can have Active Data Documents attached to them as Supporting Documents; these latter contain variable state that can be directly modified by Facilitators and other processes external to the standard Weekly Governance Cycle or Monthly Governance Cycle (i.e., the Atlas Edit Proposal process). Active Data can be lists of authorized actors, parameters, or externally collected data being prepared for data integration with the Atlas.
