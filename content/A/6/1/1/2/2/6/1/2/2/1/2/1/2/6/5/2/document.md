---
id: b838767a-5a78-47f5-9c54-b7928cb6f553
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.2
name: Get Configured Recipient
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.2 - Get Configured Recipient [Core]

The operator must look up the configured recipient for the `destinationCentrifugeId` from the `centrifugeRecipients` mapping.

`bytes32 recipient = centrifugeRecipients[destinationCentrifugeId];`
