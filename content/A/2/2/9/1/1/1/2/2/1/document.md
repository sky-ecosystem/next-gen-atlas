---
id: 8b5f1ffd-9dfd-4aa0-8fc2-638a79d9fadb
docNo: A.2.2.9.1.1.1.2.2.1
name: MaxAmount
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.2.2.9.1.1.1.2.2.1 - MaxAmount [Core]

`maxAmount` sets a hard cap on the level of allocation to an Instance at any given time. It sets the absolute rate limit regardless of how much time has passed since the last allocation. For example, if `maxAmount` is set to 1,000,000 tokens, the rate limit will increase over time at the rate determined by the `slope` until it reaches 1,000,000 tokens. At this point the rate limit will stop increasing, but it will resume increasing once an allocation to the Instance has been made.
