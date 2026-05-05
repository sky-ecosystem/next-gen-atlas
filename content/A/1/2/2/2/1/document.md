---
id: 468d192b-83bc-45ab-896f-53e8ca307135
docNo: A.1.2.2.2.1
name: The Type Specification Type
type: Type Specification
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.2.2.1 - The Type Specification Type [Type Specification]

[See below]

**Components**:

"Type Name": The Type Name Component must contain the name of the Document Type

"Type Overview": The Type Overview Component must contain high level information as human-readable text about the type, such as what it is used for and why it is necessary.

"Type Components": If the Type has Components, they must be specified in this Component as a nested object.

"Type Category": This Component must specify whether the Type is an Immutable Document, a Primary Document, a Supporting Document, or a Translation Document.

"Document Identifier Rules": This Component must specify as human-readable text rules related to the Document Identifier for Atlas Documents of this Type, and their locations in the Document Trees.

"Additional Logic": This Component can contain additional logic that applies to all Documents of the Type.

**Doc Identifier Rules**:

Type Specification Documents must follow the Document Identifier rules for Primary Documents.

**Additional Logic**:

The rules specified in Type Specification Documents must be followed for all Atlas Documents.

**Type Category**:

Primary Document

**Type Name**:

Type Specification

**Type Overview**:

The Type Specification Type is used for Type Specification Documents that specify the characteristics of each of the different Document Types. It ensures that all Type Specifications contain all necessary information to make it easy to reason about whether a document follows the requirements for its type.
