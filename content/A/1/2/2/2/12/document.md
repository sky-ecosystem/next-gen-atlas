---
id: 9ab18c94-b9b6-43d0-b260-873ad1ef66fe
docNo: A.1.2.2.2.12
name: The Facilitator Action Tenet Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.12 - The Facilitator Action Tenet Type [Type Specification]

[See below]

**Components**:

"Content": The Tenet Component specifies the adjudication logic, principle or doctrine that is directly derived from the Target Document. This Component can include policy statements underpinning the adjudication principle. Such policy statements can highlight the values that are served by, or the benefits gained from, adhering to the Tenet. When facing edge cases, these policy statements can help Facilitators to extrapolate from the Tenet's logic to achieve the most suitable outcome.

**Doc Identifier Rules**:

Facilitator Action Tenet Documents must always be located as subdocuments of the Facilitator Action Tenet Directory Document (which latter is located at position .0.4) of their Target Document. Action Tenet documents are located at the .0.4.X position, with X being the incremented number.

**Additional Logic**:

Facilitator Action Tenet Documents are likely to be necessary supplements for interpreting the Immutable Document types, as these tend to have generalized, broad language. The Core Document type has the function of operationalizing the Immutable Documents, and thus its language will tend to be far more specific and concrete. For that reason, Action Tenet Supporting Documents may not be necessary for a particular Core Document. This is not a hard-coded rule, however. The determination of whether an Action Tenet Document is needed for any given Atlas document should always be tailor-made.

Action Tenet Documents should be created and updated as necessary to reflect changes in governance practices, provide clarity on decision-making processes, and enhance understanding of governance principles and rules. The examples should not contradict their Target Document or other Supporting Documents of the Target Document.

If the Action Tenet can be anchored to a specific term from the Target Document, that term is listed first; followed by a hyphen; and then, an abstract of the Action Tenet logic, e.g.: "Organizational Drift - ACs' Mandate When Instigating Action Can Be Traced Back to a Discrete Entity". If the Action Tenet cannot be anchored to a specific term from the Target Document, the "Name" property should simply summarize the Action Tenet logic, e.g.: "Evaluating AC breach of role-specific requirement vs. general requirement".

**Type Category**:

Supporting Document

**Type Name**:

Facilitator Action Tenet

**Type Overview**:

The Facilitator Action Tenet Type is used to provide concrete adjudication principles derived from its Target Document. It distills the governance logic of the Target Document into a concise principle to guide Facilitators in resolving disputes related to the Target Document. The practical application of the Tenet is demonstrated by its "Scenario" Subdocuments.
