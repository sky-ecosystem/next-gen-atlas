---
id: 65c724f5-56d7-4ea6-a0fe-de30e6f04560
docNo: A.1.2.2.2.24
name: The Archive Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.24 - The Archive Type [Type Specification]

[See below]

**Components**:

"Original Document Type": The Type of the original document that is being archived must be specified in this component.

"Custom": Archive Documents contain Custom Components that mirror the components of the original Document at the time of the version being archived.

**Doc Identifier Rules**:

Archive Documents are located as subdocuments to the Atlas Document they are archiving. Their Document Identifier is the same as the Atlas Document they are archiving, with an additional suffix 'v' followed by the version number of the document being archived. For example, the third version of [A.1](18ac7dd3-c646-4352-9b0d-d01a2932d7d1) would have the Document Identifier A.1.v3.

**Additional Logic**:

Archive Documents should be created whenever an Atlas Document is updated to ensure that a record of all previous versions is maintained. They are not meant to be modified or deleted once created.

**Type Category**:

Accessory Document

**Type Name**:

Archive

**Type Overview**:

The Archive Type is used for storing historical versions of Atlas Documents. Archive Documents are Accessory Documents and they do not have any impact on the governance or operation of Sky, but they are important for maintaining a record of changes and evolution of the Atlas over time.
