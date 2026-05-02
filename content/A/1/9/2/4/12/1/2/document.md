---
id: 64c1fbdd-8d78-439d-810f-985734946744
docNo: A.1.9.2.4.12.1.2
name: Ecosystem Spell Validation Window
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.1.2 - Ecosystem Spell Validation Window [Core]

The Ecosystem Spell Validation Window is the period of time during which a Spell can be validated. Validation must occur:

1. After the Spell becomes visible and is available for voting on the Voting Portal (start of the validation window).
2. Before the Spell’s actions become executable, which occurs when the `GSM Pause Delay` elapses (end of the validation window).

Validation outside this window is ineffective because:

- The Spell may still be subject to changes before the start of the validation window.
- The Spell may already be executable after the end of the validation window.

The duration of the validation window is determined by the value of the GSM Pause Delay.
