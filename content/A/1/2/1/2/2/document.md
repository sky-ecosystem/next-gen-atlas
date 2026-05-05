---
id: 3263a17d-44ab-4450-af61-d797fa0c8ac7
docNo: A.1.2.1.2.2
name: Version Property
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.2.1.2.2 - Version Property [Core]

The Version property of Atlas Documents specifies how many times it has been modified. Every time an Atlas Document is modified, the newly modified Document gets its version number incremented, and the old version is recorded as a historical version with a Document Identifier equivalent to its version number.

As an example, if an Atlas Document located at 1.1.1 with version number 3 is modified, the new Atlas Document will have version number 4, and the old Atlas Document will be located at 1.1.1.v3.

This ensures all historical versions of Atlas documents are retained permanently as a part of the Atlas.
