---
id: c0c0d3cb-389e-4dc7-a475-e9bbb5bf633f
docNo: A.1.2.2.2.18
name: The Budget Controller Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.18 - The Budget Controller Type [Type Specification]

[See below]

**Components**:

"Content": The Content Component of Budget Controller Documents is used to describe flexible rules of how the Active Data Documents and Budget Documents must behave, and how they can be modified. The Custom Components format and requirements of the Active Data Documents and the Budget Documents must be defined as well.

**Doc Identifier Rules**:

Budget Controller Documents follow the Document Identifier Rules of Primary Documents.

**Additional Logic**:

Budget Controller Documents must have an Active Data Directory Document located below it at the .0.6 position, and a Budget Directory Document located below it at the .0.7 position.

**Type Category**:

Primary Document

**Type Name**:

Budget Controller

**Type Overview**:

The Budget Controller Type is used to manage the budgets used by Sky to operationalize the Scopes to achieve the purpose and goals of the Spirit of the Atlas. It controls variable state that specifically authorizes executive votes to disburse payments from the Sky Surplus Buffer, or authorize smart contracts to disburse such payments. The Budget Controller Document determines the rules and processes for modifying and using the budgets contained in the Budget Documents that are attached to it. Budget Controllers also have Active Data Documents attached that are used to report on the status and results of projects funded through the Budget Documents.
