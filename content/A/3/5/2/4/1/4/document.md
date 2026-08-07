---
id: 6c389eb2-8f50-4b6b-ad77-deb27c9f9fb0
docNo: A.3.5.2.4.1.4
name: Tau Definition
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.5.2.4.1.4 - Tau Definition [Core]

The `tau` parameter defines the minimum time interval, in seconds, that must elapse between consecutive uses or operations of the SBE-BEAM.

A SBE-BEAM operation may adjust one or more parameters. Once a SBE-BEAM operation is executed, the `tau` duration must expire before any subsequent SBE-BEAM operation can be performed. This interval applies to every operation regardless of whether it raises or lowers the affected parameters.
