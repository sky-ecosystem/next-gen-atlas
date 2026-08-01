---
id: 79cb1503-2f4f-4367-b9c9-71a5dddb39fa
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.4
name: Check Recipient Configured
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.4 - Check Recipient Configured [Core]

The operator must ensure a recipient is configured for the `destinationCentrifugeId`. The action reverts with `centrifuge-id-not-configured` if the recipient is unset.

`require(recipient != 0, "MainnetController/centrifuge-id-not-configured");`
