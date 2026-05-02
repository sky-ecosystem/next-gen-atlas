---
id: 6423437d-d062-4a4f-ac03-7f056938d3c6
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.3
name: Initiate Smaller Transactions If Needed
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.3 - Initiate Smaller Transactions If Needed [Core]

If `usdcAmount` exceeds the per-message limit, the transfer must be split into multiple smaller batches executing the following loop until the remaining amount is less than or equal to the limit.

1. The operator must transfer the maximum allowed (`burnLimit`) using `_initiateCCTPTransfer`.
2. The operator must reduce the remaining `usdcAmount` by the `burnLimit`.

`while (usdcAmount > burnLimit) {
    _initiateCCTPTransfer(burnLimit, destinationDomain, mintRecipient);
    usdcAmount -= burnLimit;
}`
