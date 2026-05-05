---
id: f46cbe06-e7df-4a92-8972-cd21bf9be2c5
docNo: A.6.1.1.6.2.6.1.2.2.1.3.1
name: Get Rate Limit Data
type: Core
depth: 13
childType: sections_and_primary_docs
---

###### A.6.1.1.6.2.6.1.2.2.1.3.1 - Get Rate Limit Data [Core]

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored RateLimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory)`
