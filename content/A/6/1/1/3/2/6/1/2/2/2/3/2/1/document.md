---
id: 4f8c8aa3-fffc-46dd-aeb7-b23e996619d7
docNo: A.6.1.1.3.2.6.1.2.2.2.3.2.1
name: Full Freeze
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.3.2.1 - Full Freeze [Core]

This action leads to a complete freeze and prevents any actions on the Controller until the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) subsequently lifts this status. Integrations, Reserves nor Permissions cannot be managed during this period, and funds cannot be moved.

`manage_controller(
ManageControllerArgs {
status: ControllerStatus::PushPullFrozen,
}
)`
