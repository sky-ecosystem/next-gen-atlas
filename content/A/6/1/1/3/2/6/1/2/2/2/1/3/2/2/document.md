---
id: 62654961-cf70-4455-a7df-c81861944395
docNo: A.6.1.1.3.2.6.1.2.2.2.1.3.2.2
name: Set Rate Limit Data
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.2 - Set Rate Limit Data [Core]

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set or update rate limit data for a specific `Integration`, including `rate_limit_slope` and `rate_limit_max_outflow`.

`manage_integration(
ManageIntegrationArgs {
status: None,
description: None,
rate_limit_slope: Some(rate_limit_slope),
rate_limit_max_outflow: Some(rate_limit_max_outflow),
}
)`
