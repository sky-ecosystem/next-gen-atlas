---
id: 2ed41eef-989b-4253-8de7-5e368da0242a
docNo: A.6.1.1.3.2.6.1.2.2.2.3.2.2
name: Reallocation Freeze
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.3.2.2 - Reallocation Freeze [Core]

A complete freeze prevents any movement of funds within the Controller until the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) subsequently lifts this status. Integrations, Reserves and Permissions cannot be configured during this period.

`manage_controller(
ManageControllerArgs {
status: ControllerStatus::Frozen,
}
)`
