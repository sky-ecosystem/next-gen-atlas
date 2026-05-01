---
id: c75e8c0d-0b16-4808-a14c-dac919ef9269
docNo: A.6.1.1.3.2.6.1.2.2.2.1.3.2.1
name: Get Rate Limit Data
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.1 - Get Rate Limit Data [Core]

The properties associated with a Reserve level rate limit can be read from the `Integration` account corresponding to a particular token, as follows:

`pub struct Integration {
// ...
pub rate_limit_slope: u64,
pub rate_limit_max_outflow: u64,
pub rate_limit_outflow_amount_available: u64,
pub rate_limit_remainder: u64
// ...
}`
