---
id: bd904ac0-32d2-4592-92cd-3eb01a3ce7de
docNo: A.6.1.1.3.2.6.1.2.2.2.1.3.2.3
name: Set Unlimited Rate Limit Data
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.3 - Set Unlimited Rate Limit Data [Core]

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set unlimited rate limit data for a specific key by configuring it with maximum values.

`manage_integration(
ManageIntegrationArgs {
status: None,
description: None,
rate_limit_slope: Some(0),
rate_limit_max_outflow: Some(u64::MAX),
}
)`
