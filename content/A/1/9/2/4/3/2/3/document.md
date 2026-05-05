---
id: b97f9d90-82cd-4ca8-a78f-a7e9c115a4f5
docNo: A.1.9.2.4.3.2.3
name: Checksums
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.3.2.3 - Checksums [Core]

The total amount of token transfers must always be summed up in the Executive Sheet. The Governance Point and Technical Point independently sum up the value. The value of USDS and Dai must always be expressed as integers, with no decimal places, due to tests and helper functions used by developers requiring integer values. For USDS and Dai, values must always be rounded up to ensure recipients receive at least the expected amount. The values of SKY and other tokens must be listed to exactly two decimal places. All summations must occur only after the Executive Sheet is complete to avoid missing any transfers.
