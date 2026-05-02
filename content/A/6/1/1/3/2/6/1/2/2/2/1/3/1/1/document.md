---
id: 21590f17-8e03-4fc3-9a37-e8364bbee322
docNo: A.6.1.1.3.2.6.1.2.2.2.1.3.1.1
name: Get Rate Limit Data
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.3.1.1 - Get Rate Limit Data [Core]

The properties associated with a Reserve level rate limit can be read from the `Reserve` account corresponding to a particular token, as follows:

`pub struct Reserve {
// ...
pub rate_limit_slope: u64,
pub rate_limit_max_outflow: u64,
pub rate_limit_outflow_amount_available: u64,
pub rate_limit_remainder: u64
// ...
}`
