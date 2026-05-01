---
id: 6ae438cd-3678-46a2-b323-1f44204b5759
docNo: A.1.2.1.2.5
name: Components Property
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.1.2.5 - Components Property [Core]

The Components property of Atlas Documents contains an object that specifies the data components of the Atlas Document as nested properties. The Components of an Atlas Document is determined by its Type. Some Document Types have no Components, in which the object is just empty.

An Atlas Document with Components must always have all of its components properly filled according to the requirements defined by its Type Specification. Some documents have custom logic for how their Components behave, and this custom logic is specified through a special reserved component property called 'Custom'. Atlas Documents of Types with specified custom logic components can have variable number of components, and different characteristics of each component, for each instance of the Type. Custom components are always appended to the end of the list of components.
