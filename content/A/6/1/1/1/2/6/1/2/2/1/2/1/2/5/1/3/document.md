---
id: 469d9616-010c-4648-8fc4-66eeff7398c3
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.3
name: Verify Mint Recipient
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.3 - Verify Mint Recipient [Core]

** **The operator must verify the `mint` recipient. They must check that a mint recipient (mapping from domain IDs to recipient addresses) is configured for the `destinationDomain`. If no recipient is configured, the transaction will revert with an error message.

`bytes32 mintRecipient = mintRecipients[destinationDomain];
require(mintRecipient != 0, "MainnetController/domain-not-configured");`
