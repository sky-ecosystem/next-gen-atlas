---
id: 921dd8b4-763e-4edf-9cb9-f2e0cb012109
docNo: A.6.1.1.3.2.6.1.2.2.1.1.3.1
name: Get Rate Limit Data
type: Core
depth: 14
childType: sections_and_primary_docs
---

###### A.6.1.1.3.2.6.1.2.2.1.1.3.1 - Get Rate Limit Data [Core]

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored Rate LimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRate LimitData(bytes32 key) external override view returns (Rate LimitData memory)`
