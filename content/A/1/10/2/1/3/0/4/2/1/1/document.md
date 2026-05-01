---
id: 1ebcda5d-5a10-4e78-ba52-5772df38cc56
docNo: A.1.10.2.1.3.0.4.2.1.1
name: Delay In Payment To Ranked Delegate Triggering Proposal
type: Scenario
depth: 11
childType: tenets
---

###### A.1.10.2.1.3.0.4.2.1.1 - Delay In Payment To Ranked Delegate Triggering Proposal [Scenario]

**Description**:

Entity is a Ranked Delegate with at least the Triggering Threshold in their AD Buffer. Entity triggers a Weekly Cycle Proposal. Immediately thereafter, Entity loses their Ranked Delegate rank. Three days later, before the Proposal has been voted on, the Core Facilitator distributes compensation to other Aligned Delegates but does not distribute compensation to Entity.

**Finding**:

Aligned

**Additional Guidance**:

Paying out the AD Buffer would have led to Entity's AD Buffer dropping below the required Triggering Threshold while the Proposal was still unresolved. In this Scenario, the triggering AD cannot receive payout from the AD Buffer until the triggered Proposal is voted on and approved by Sky Governance. Assuming that the Proposal is approved, the Core Facilitator is authorized to disburse the entire contents of the AD Buffer to the triggering AD in the next AD compensation cycle. However, if the Proposal is rejected by the Core Facilitator for misalignment or voted down by Sky Governance, the triggering AD loses an amount of USDS from their AD Buffer equal to the Triggering Threshold.
