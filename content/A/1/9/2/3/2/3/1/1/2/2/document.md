---
id: 3deb3282-434c-4d56-b5e3-3a4daad3cd1d
docNo: A.1.9.2.3.2.3.1.1.2.2
name: Responsibilities For Agents
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.1.9.2.3.2.3.1.1.2.2 - Responsibilities For Agents [Core]

The Agents are required to include logic for the public view method `isExecutable()` in their Spell. This function is used to signal if the Spell is ready to be executed in a particular block or not. StarGuard cannot execute an Agent Spell if `isExecutable()` returns `False`. The value that must be returned for execution to be possible is `True`.
