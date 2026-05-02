---
id: 71db0980-a49f-4d48-b277-87f9a2340a8f
docNo: A.1.2.2.2.10
name: The Element Annotation Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.10 - The Element Annotation Type [Type Specification]

[See below]

**Components**:

"Element": The Element Component should contain the unique word or phrase from the Target Document that is being annotated.

"Annotation": The Annotation Component should concisely disambiguate and bound the semantic meaning of problematic terms in the Target Document. Such terms can be vague, ambiguous or technical jargon specific to the Target Document.

**Doc Identifier Rules**:

Element Annotation Documents must always be located as subdocuments to the Element Annotation Directory Document of their Target Document. Element Annotation documents are located at the .0.3.X position, with X being the incremented number.

**Additional Logic**:

Element Annotation Documents should be updated as necessary to reflect changes in the understanding or interpretation of the Element and/or any related Atlas document, while maintaining consistency with the Target Document. The Element Annotation should not contradict its Target Document or other context data of the Target Document.

The "Name" property of each Element Annotation Document instance must follow a standardized template: the annotated Element is listed first, followed by a hyphen, and the phrase "Element Annotation".

**Type Category**:

Supporting Document

**Type Name**:

Element Annotation

**Type Overview**:

Element Annotation Documents provide further specification of the semantic meaning of vague or ambiguous terms in the Target Document. Element Annotation Documents can also briefly define technical jargon that is unique to the Target Document. Element Annotation Documents can be thought of as serving a function similar to that of a footnote: they can provide useful context or commentary. Element Annotations should be as concise as possible.
