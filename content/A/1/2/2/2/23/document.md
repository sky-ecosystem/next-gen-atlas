---
id: dde9bb23-9ba2-4de6-a3fe-3093e5108fa4
docNo: A.1.2.2.2.23
name: The Translation Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.23 - The Translation Type [Type Specification]

[See below]

**Components**:

"Original Document Type": The Type of the original document that is being translated must be specified in this component.

"Language": The Language Component specifies the language in which the Atlas Document is translated.

"Translated Name": The Translated Name component contains the name of the translated Atlas Document in the new language.

 "Custom": Translation Documents contain Custom Components that mirror the components of the original Document with component name and component data translated to the new language.

**Doc Identifier Rules**:

Translation Documents are located as subdocuments to the Atlas Document they are translating. Their Document Identifier is the same as the Atlas Document they are translating, with an additional suffix that represents the language of the translation. For example, a Spanish translation of [A.1](18ac7dd3-c646-4352-9b0d-d01a2932d7d1) would have the Document Identifier A.1.es.

**Additional Logic**:

Translation Documents should be updated whenever the Atlas Document they are translating is updated to ensure that the translation remains accurate. However, in case of any discrepancies or contradictions, the original English version of the Atlas Document always takes precedence.

**Type Category**:

Accessory Document

**Type Name**:

Translation

**Type Overview**:

The Translation Type is used for creating translated versions of Atlas Documents to make the Atlas accessible to non-English speakers. Translation Documents are Accessory Documents and they do not have any impact on the governance or operation of Sky, but they are important for accessibility and inclusivity.
