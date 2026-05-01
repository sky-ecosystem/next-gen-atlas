---
id: e06f6a83-7c74-4abd-b4da-771cbfdf2fb9
docNo: A.1.9.2.4.13.3
name: Execution Setup For Approved Vote
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.9.2.4.13.3 - Execution Setup For Approved Vote [Core]

If the executive is approved and has been lifted to become the current hat in the DSChief, a future action to execute the Spell's actions is prepared by calling `schedule()` on the Spell contract. This action is permissionless, meaning any Ethereum address can trigger the execution without requiring special permissions. This process involves calling `plot` on `ds-pause` with four parameters related to the Spell action contract:

- The address of the Spell action contract.
- The `extcodehash` value of the Spell action contract.
- Any `calldata` information required for the future execution of the Spell contract's actions using `execute()`.
- The `eta`, which is the earliest time the Spell's actions can be executed. This must be scheduled at least the duration of the pause delay into the future.

Once the Spell's actions are "plotted" in the Pause, the Spell is considered `scheduled`, and the countdown to the `eta` time begins. In the absence of Office Hours, this countdown is typically equal to the duration of the `GSM Pause Delay`. If Office Hours are set to "Yes" then the countdown will be equal to the `GSM Pause Delay` plus whatever time is needed to enter the Office Hours window.
