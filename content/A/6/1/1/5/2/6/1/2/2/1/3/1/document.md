---
id: 716b493e-d102-47c8-8f87-bcb1c809c8ee
docNo: A.6.1.1.5.2.6.1.2.2.1.3.1
name: Get Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.5.2.6.1.2.2.1.3.1 - Get Rate Limit Data [Core]

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored Rate LimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRate LimitData(bytes32 key) external override view returns (Rate LimitData memory)`
