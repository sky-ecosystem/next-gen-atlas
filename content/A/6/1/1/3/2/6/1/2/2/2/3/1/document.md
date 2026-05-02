---
id: c4932ae7-0bf2-46fe-bbca-4bdd675368c9
docNo: A.6.1.1.3.2.6.1.2.2.2.3.1
name: Remove Compromised Relayer As Freezer
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]

In the event of a compromised Relayer, the [A.6.1.1.3.2.6.1.2.2.2.1.1.3 - Freezer Role](6f7becc7-2e70-44e5-8662-25ba7dd1a5f8) and [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) can call the instruction to suspend the compromised Relayer from the Controller program, thereby preventing it from doing any further harm to the system. The backstop Relayer can then take over. This function should only be used if the keys to the Relayer multisig have been leaked or compromised, and the Relayer is now in the hands of an external bad actor.

`manage_permission(
ManagePermissionArgs {
status: PermissionStatus::Suspended,
can_manage_permissions: false,
can_invoke_external_transfer: false,
can_execute_swap: false,
can_reallocate: false,
can_freeze_controller: false,
can_unfreeze_controller: false,
can_manage_reserves_and_integrations: false,
can_suspend_permissions: false,
can_liquidate: false,
}
)`
